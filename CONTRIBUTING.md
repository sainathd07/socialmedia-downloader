# Contributing to Social Media Downloader

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
git clone https://github.com/sainathd07/socialmedia-downloader.git
cd socialmedia-downloader
   ```
3. **Set up development environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements-dev.txt
   ```

## Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**

3. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

## Code Standards

### Python Style
- Follow PEP 8
- Use type hints
- Add docstrings to all functions
- Keep functions focused and small

### Testing
- Add tests for new features
- Ensure all tests pass before submitting PR
- Aim for >80% code coverage

### Documentation
- Update README.md if needed
- Add docstrings to new functions
- Update USER_GUIDE.md for user-facing changes

## Commit Message Format

Use conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Adding tests
- `refactor:` Code refactoring
- `style:` Code formatting
- `chore:` Maintenance tasks

Examples:
```
feat: add TikTok support
fix: handle network timeout errors
docs: update installation instructions
test: add integration tests for Instagram
```

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG** (if exists)
5. **Describe your changes** clearly in PR description

### PR Description Template:

```markdown
## What does this PR do?
Brief description of changes

## Why is this change needed?
Context and motivation

## How was this tested?
- [ ] Unit tests added
- [ ] Manual testing completed
- [ ] All tests pass

## Screenshots (if UI changes)
[Add screenshots here]

## Checklist
- [ ] Code follows project style
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests passing
```

## Areas for Contribution

### High Priority
- [ ] Additional platform support (TikTok, Twitter, Vimeo)
- [ ] Batch download functionality
- [ ] Download history database
- [ ] GUI component tests
- [ ] Windows/Linux testing and bug fixes

### Medium Priority
- [ ] Thumbnail preview
- [ ] Subtitle download options
- [ ] Proxy support
- [ ] Resume interrupted downloads
- [ ] Playlist support

### Low Priority
- [ ] Custom themes
- [ ] Keyboard shortcuts
- [ ] Browser extension
- [ ] Scheduled downloads
- [ ] Cloud storage integration

## Testing

### Running Tests Locally

```bash
# All tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=src --cov-report=html

# Specific test file
pytest tests/test_validator.py -v
```

### Manual Testing Checklist

- [ ] YouTube video download
- [ ] YouTube audio download
- [ ] Instagram post download
- [ ] Invalid URL handling
- [ ] Progress tracking accuracy
- [ ] Settings persistence
- [ ] Dark/light mode toggle
- [ ] Custom folder selection

## Building

### Local Build

```bash
# macOS
./build.sh

# Windows
build_windows.bat

# Test built app
open dist/VideoDownloader.app  # macOS
```

## Code Review Guidelines

All PRs will be reviewed for:

- Code quality and style
- Test coverage
- Documentation completeness
- Performance impact
- Security considerations
- User experience

## Reporting Bugs

### Before Reporting

1. Check existing issues
2. Try latest version
3. Read TROUBLESHOOTING.md
4. Check if it's a known limitation

### Bug Report Template

```markdown
**Describe the bug**
Clear description of what's wrong

**To Reproduce**
1. Step 1
2. Step 2
3. Error occurs

**Expected behavior**
What should happen

**Screenshots**
If applicable

**Environment:**
- OS: [e.g., macOS 13.0]
- App Version: [e.g., 1.0.0]
- Python Version: [e.g., 3.12]
- FFmpeg installed: [Yes/No]

**Logs**
Paste relevant logs from ~/.video_downloader/logs/

**Additional context**
Any other relevant information
```

## Feature Requests

Feature requests are welcome! Please:

1. Check if already requested
2. Explain the use case
3. Provide examples
4. Consider implementation complexity

### Feature Request Template

```markdown
**Feature Description**
What feature do you want?

**Use Case**
Why is this useful?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you thought of

**Additional Context**
Screenshots, examples, etc.
```

## Questions?

- Open an issue for questions
- Check existing documentation
- Read the development guide

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

- Be respectful and professional
- Welcome newcomers
- Focus on constructive feedback
- Help maintain a positive community

## Thank You!

Your contributions make this project better for everyone! 🎉
