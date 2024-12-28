# $CHECK Repository Authenticity Tool

An open-source tool from the $CHECK ecosystem designed to verify GitHub repository authenticity and detect code plagiarism. This tool helps maintain integrity in the blockchain space by analyzing repositories for feature implementation, code similarity, and overall health.

## Features

- **Deep Analysis Engine**: Advanced repository scanning to verify claimed features against actual implementations
- **Plagiarism Detection**: Sophisticated algorithms to identify code similarity patterns and potential plagiarism
- **Health Verification**: Comprehensive checks for repository maintenance and security status
- **Feature Verification**: Analyzes repository claims against actual codebase implementation
- **Similarity Scanning**: Detects potential code copying and unauthorized reuse
- **Health Assessment**: Evaluates repository maintenance, documentation, and security practices

## Prerequisites

- Python 3.8 or higher
- GitHub Personal Access Token (for API access)
- Git installed on your system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CheckItSOL/LARPCHECK.git
cd LARPCHECK
```

2. Create and activate a virtual environment (recommended):
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

The tool uses the following main dependencies:
- `PyGithub`: GitHub API interaction
- `scikit-learn`: Code similarity analysis
- `nltk`: Natural language processing for feature analysis
- `python-dotenv`: Environment variable management
- `colorama` & `termcolor`: Terminal output styling
- `halo`: Terminal spinners

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your GitHub token to `.env`:
   ```
   GITHUB_TOKEN=your_github_token_here
   ```

   To get a GitHub token:
   1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   2. Click "Generate new token" → "Generate new token (classic)"
   3. Give it a name and select the following scopes:
      - `repo` (Full control of private repositories)
      - `read:packages` (Read access to packages)
   4. Copy the generated token and paste it in your `.env` file

## Usage

1. Run the tool:
```bash
python main.py
```

2. Enter the GitHub repository URL when prompted

3. The tool will perform:
   - Repository feature analysis
   - Code similarity detection
   - Health and security checks
   - Maintenance status verification

## Example Output

```
╔════════════════════════════════════════════╗
║           Repository Analysis              ║
╚════════════════════════════════════════════╝

Repository: username/repo
URL: https://github.com/username/repo

[Feature Analysis]
✓ Authentication System
  - Implementation found in auth/
  - Tests present
✗ Real-time Updates
  - No implementation found
  - Feature claimed but not verified

[Similarity Detection]
! 85% similarity with other/repo
  → Matching patterns in:
    - src/core/
    - utils/helpers.js

[Health Assessment]
✓ Active Development
✓ Security Measures
✓ Documentation
✗ Test Coverage (65%)

Status: VERIFICATION REQUIRED
```

## Configuration

The tool can be configured through environment variables in your `.env` file:

```env
# Required
GITHUB_TOKEN=your_github_token_here

# Optional
SIMILARITY_THRESHOLD=0.8  # Minimum similarity score to flag repositories (0.0 to 1.0)
SCAN_DEPTH=3             # How deep to scan repository history
VERIFY_TESTS=true        # Whether to verify test coverage
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with 💜 by the $CHECK team
