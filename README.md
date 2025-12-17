# AI-Powered Startup Idea Validation System

A multi-agent framework using CrewAI for automated startup validation, market research, and pitch development.

## Overview

This system employs five specialized AI agents that collaboratively transform raw startup concepts into comprehensive business proposals with market research, product specifications, go-to-market strategies, and investor pitch materials.

## Features

- **Automated Idea Refinement**: Clarifies problems, target users, and differentiation
- **Market Research**: Performs competitive analysis and market sizing using web search
- **Product Specification**: Generates MVP specs with prioritized features
- **Go-to-Market Strategy**: Develops customer profiles and acquisition channels
- **Investor Pitch Generation**: Creates structured investor memo in markdown format

## System Architecture

### Multi-Agent Pipeline
```
User Idea → Startup Strategist → Market Researcher → Product Designer → Growth Marketer → Funding Analyst → Pitch Output
```

### Agents

1. **Startup Strategist** - Refines concepts and identifies key assumptions
2. **Market Researcher** - Conducts competitive and market analysis
3. **Product Designer** - Creates MVP specifications and roadmaps
4. **Growth Marketer** - Develops GTM strategy and landing page copy
5. **Funding Analyst** - Compiles investor-ready pitch materials

## Installation

### Prerequisites

- Python 3.8+
- API Keys:
  - SerperDev API key (for web search)
  - LLM API credentials (OpenAI, Anthropic, etc.)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd startup-crew
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```bash
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key  # or other LLM provider
```

## Usage

Run the system:
```bash
python -m src.run
```

Enter your startup idea when prompted (2-5 sentences).

The system will:
1. Process your idea through all five agents
2. Display progress and intermediate outputs
3. Generate final pitch outline as `startup_pitch_outline.md`

## Project Structure
```
startup-crew/
├── src/
│   ├── __init__.py
│   ├── agents.py          # Agent definitions
│   ├── tasks.py           # Task specifications
│   ├── crew.py            # Crew orchestration
│   ├── tools.py           # External tool configs
│   └── run.py             # Entry point
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
└── README.md
```

## Dependencies
```
crewai
crewai-tools
python-dotenv
duckduckgo-search
requests
litellm
```

## Output

The system generates:
- **Console Output**: Real-time agent reasoning and intermediate results
- **Pitch Outline File**: `startup_pitch_outline.md` with complete validation report

### Output Sections

1. Problem & Solution
2. Market & Competition
3. Product & Roadmap
4. GTM Strategy
5. Business Model & Key Metrics

## Configuration

### Agent Customization

Edit `src/agents.py` to modify:
- Agent roles and goals
- Backstories and expertise
- Tool assignments

### Task Customization

Edit `src/tasks.py` to adjust:
- Task descriptions and prompts
- Expected output formats
- Context dependencies

### Workflow Customization

Edit `src/crew.py` to change:
- Agent sequence
- Process type (sequential/hierarchical)
- Task dependencies

## Example
```python
# Input
"A mobile app that helps remote workers find coworking spaces 
in their city with real-time availability and booking."

# Output
- Refined concept with clear problem-solution fit
- Market size estimates and competitor analysis
- MVP feature list and tech stack recommendations
- Landing page copy and acquisition channels
- Investor pitch outline ready for deck creation
```

## Use Cases

- **Founders**: Validate and structure startup ideas systematically
- **Investors**: Perform initial due diligence on concepts
- **Accelerators**: Standardize idea evaluation processes
- **Educators**: Teach entrepreneurship frameworks
- **Consultants**: Streamline business planning engagements

## Limitations

- Sequential processing only (no parallel execution)
- Depends on external API availability
- No automated fact-checking
- Text-based outputs only
- Fixed workflow structure

## Future Enhancements

- [ ] Financial modeling integration
- [ ] Technical feasibility assessment
- [ ] Iterative validation loops
- [ ] Web interface for non-technical users
- [ ] Integration with business planning tools
- [ ] Custom agent creation interface
- [ ] Multi-language support

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Your License Here]

## Support

For issues and questions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

## Acknowledgments

- Built with [CrewAI](https://www.crewai.com/)
- Search powered by [SerperDev](https://serper.dev/)
- LLM interface via [LiteLLM](https://docs.litellm.ai/)

## Citation

If you use this project in your research or work, please cite:
```
Revanth Reddy kanubaddi. (2025). AI-Powered Startup Idea Validation System. 
GitHub repository: https://github.com/revanthreddy24/Start-up-advisor-using-crew-ai
```

---

**Version**: 1.0.0  
**Last Updated**: December 2025
