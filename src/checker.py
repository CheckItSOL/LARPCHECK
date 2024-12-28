import re
from github import Github
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from halo import Halo
from datetime import datetime, timedelta
import os

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

class LARPChecker:
    def __init__(self, repo_url):
        self.g = Github(GITHUB_TOKEN)
        self.repo_url = repo_url
        self.repo_name = self.extract_repo_name(repo_url)
        self.repo = self.g.get_repo(self.repo_name)
        self.features = []
        self.similar_repos = []
        
    def extract_repo_name(self, url):
        """Extract repository name from GitHub URL"""
        pattern = r'github\.com/(.+/.+?)(?:\.git)?$'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        raise ValueError("Invalid GitHub URL")

    def analyze_features(self):
        """Analyze repository for promised features"""
        try:
            spinner = Halo(text='Analyzing repository features', spinner='dots', color='cyan')
            spinner.start()
            
            readme = self.repo.get_readme()
            readme_content = readme.decoded_content.decode()
            
            features = []
            lines = readme_content.split('\n')
            for line in lines:
                if re.match(r'^#+\s+Features', line, re.I):
                    features.append(("Feature Section Found", True))
                if re.match(r'[-*]\s+', line):
                    feature = re.sub(r'[-*]\s+', '', line).strip()
                    if feature:
                        features.append((feature, self._verify_feature(feature)))
            
            self.features = features
            spinner.succeed('Feature analysis complete')
            return features
        except Exception as e:
            spinner.fail(f'Error analyzing features: {str(e)}')
            return [("Error analyzing features", str(e))]

    def _verify_feature(self, feature):
        """Verify if a feature appears to be implemented"""
        try:
            keywords = word_tokenize(feature.lower())
            keywords = [word for word in keywords if word not in stopwords.words('english')]
            
            code_found = False
            for keyword in keywords:
                results = self.repo.get_contents("")
                for content in results:
                    if content.type == "file" and content.name.endswith(('.py', '.js', '.java', '.cpp', '.go')):
                        file_content = content.decoded_content.decode()
                        if keyword in file_content.lower():
                            code_found = True
                            break
                if code_found:
                    break
            
            return code_found
        except:
            return False

    def check_code_similarity(self, limit=5):
        """Check for similar repositories"""
        try:
            spinner = Halo(text='Scanning for similar repositories', spinner='dots', color='magenta')
            spinner.start()
            
            repo_content = self._get_repo_content()
            similar_repos = []
            keywords = ' '.join(self.repo.get_topics())
            if not keywords:
                keywords = self.repo.name
            
            for repo in self.g.search_repositories(keywords, sort='stars'):
                if repo.full_name != self.repo_name and len(similar_repos) < limit:
                    similar_content = self._get_repo_content(repo)
                    if similar_content:
                        similarity = self._calculate_similarity(repo_content, similar_content)
                        if similarity > 0.8:
                            similar_repos.append({
                                'repo': repo.full_name,
                                'similarity': similarity,
                                'url': repo.html_url
                            })
            
            self.similar_repos = similar_repos
            spinner.succeed('Similarity analysis complete')
            return similar_repos
        except Exception as e:
            spinner.fail(f'Error checking similarity: {str(e)}')
            return [{"error": str(e)}]

    def _get_repo_content(self, repo=None):
        """Get concatenated content of main code files"""
        if repo is None:
            repo = self.repo
        try:
            content = []
            results = repo.get_contents("")
            for item in results:
                if item.type == "file" and item.name.endswith(('.py', '.js', '.java', '.cpp', '.go')):
                    content.append(item.decoded_content.decode())
            return '\n'.join(content)
        except:
            return ""

    def _calculate_similarity(self, content1, content2):
        """Calculate cosine similarity between two code contents"""
        vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b')
        try:
            tfidf_matrix = vectorizer.fit_transform([content1, content2])
            return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        except:
            return 0.0

    def generate_report(self):
        """Generate a comprehensive report"""
        spinner = Halo(text='Generating analysis report', spinner='dots', color='cyan')
        spinner.start()
        
        report = {
            'repository': {
                'name': self.repo_name,
                'url': self.repo_url,
                'stars': self.repo.stargazers_count,
                'forks': self.repo.forks_count,
                'last_updated': self.repo.updated_at.strftime('%Y-%m-%d')
            },
            'features_analysis': self.features,
            'similar_repositories': self.similar_repos,
            'health_checks': {
                'has_readme': bool(self.repo.get_readme()),
                'has_license': bool(self.repo.get_license()),
                'has_tests': self._has_tests(),
                'active_development': self._check_active_development()
            }
        }
        
        spinner.succeed('Report generated')
        return report

    def _has_tests(self):
        """Check if repository has tests"""
        try:
            test_patterns = ['test', 'spec', 'tests']
            for pattern in test_patterns:
                results = self.repo.get_contents("")
                for content in results:
                    if pattern in content.name.lower():
                        return True
            return False
        except:
            return False

    def _check_active_development(self):
        """Check if repository is actively maintained"""
        try:
            commits = self.repo.get_commits()
            last_commit = commits[0].commit.author.date
            three_months_ago = datetime.now() - timedelta(days=90)
            return last_commit > three_months_ago
        except:
            return False
