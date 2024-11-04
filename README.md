
# AWS Dynamic Documentation with LLM

An open-source project that generates dynamic documentation for AWS infrastructure using Large Language Models (LLMs). This tool allows users to inspect and document AWS resources across multiple accounts and regions, providing an interactive interface for creating, viewing, and exporting documentation.

## Project Overview

The application connects to AWS accounts to retrieve infrastructure information (EC2, S3, RDS, etc.) and uses an LLM to interpret and document configurations, dependencies, and best practices. Users can interact with a local web interface to run queries, generate documentation, and export it in various formats.

## Features

- **Multi-Account and Multi-Region Support**: Select a single AWS account or multiple accounts, as well as specific regions or all regions.
- **Interactive Query Interface**: Enter custom queries to retrieve specific information about AWS resources.
- **Automated Documentation with LLM**: The LLM interprets data from AWS and generates easy-to-read documentation.
- **Export Options**: Save documentation in PDF or Markdown format.
- **No Login Required**: Start using the tool immediately without an authentication step.

## Project Structure

```plaintext
aws-doc-llm/
├── app.py                    # Main file to start the Flask server
├── config/
│   ├── aws_config.py         # Manages AWS account configurations and credentials
│   └── settings.py           # General project settings (e.g., server port, global variables)
├── controllers/
│   ├── query_handler.py      # Handles queries, integrating LLM and AWS calls
│   └── export_handler.py     # Responsible for exporting generated documentation (PDF, Markdown, etc.)
├── templates/
│   └── index.html            # Initial HTML interface (using Bootstrap optionally)
├── static/
│   ├── css/                  # CSS files for the graphical interface
│   └── js/                   # JavaScript files for interactivity
├── utils/
│   ├── aws_helpers.py        # Helper functions to connect and retrieve data from AWS
│   └── llm_helpers.py        # Helper functions to integrate with LLMs
└── requirements.txt          # Project dependencies (Flask, boto3, Streamlit, etc.)
```

### Components

- **app.py**: The main entry point that initializes the Flask server and defines application routes.
- **config/**:
  - **aws_config.py**: Manages AWS account configurations, including adding, listing, and removing accounts.
  - **settings.py**: Stores general settings like server port and default configurations.
- **controllers/**:
  - **query_handler.py**: Processes interface queries, integrating LLM and AWS calls.
  - **export_handler.py**: Manages export functionality for documentation in various formats.
- **templates/**: Contains HTML templates for the web interface (starting with `index.html`).
- **static/**: Stores static files (CSS and JavaScript) for front-end styling and interactivity.
- **utils/**:
  - **aws_helpers.py**: Contains helper functions to connect to AWS and retrieve resource information.
  - **llm_helpers.py**: Integrates with the LLM, sending prompts and receiving responses.
- **requirements.txt**: Lists dependencies like Flask, boto3, Streamlit, and other libraries.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **AWS CLI**: Required for setting up and managing AWS credentials locally. [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) and configure it by running `aws configure`.
- **AWS Access Keys**: Required for the AWS accounts you intend to document.
- **Ollama 3.2**: Required for the LLM functionality. **Ollama** must be installed on your system to execute this project.

### Ollama Installation

To install Ollama, follow these steps:

1. **Install Ollama** (for macOS):

   ```bash
   brew install ollama/tap/ollama
   ```

2. **Verify Installation**:

   ```bash
   ollama version
   ```

   Ensure that the version is 3.2, as this is required for the project.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/aws-doc-llm.git
   cd aws-doc-llm
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up AWS credentials**:

   Configure AWS credentials using the AWS CLI with the command:

   ```bash
   aws configure
   ```

   Alternatively, you can manually configure the credentials in the `aws_config.py` file.

4. **Run the application**:

   ```bash
   make run
   ```

5. **Access the local server**:

   Open `http://localhost:5000` in your browser to start using the tool.

### Usage

1. **Select AWS Account and Region(s)**:
   Choose an AWS account and region (or select "All Regions") to define the scope of the query.

2. **Enter a Query**:
   Use the query box to specify what you want to document (e.g., "List all EC2 instances and security groups").

3. **View and Export Documentation**:
   View the generated documentation directly on the interface, and export it in PDF or Markdown as needed.

4. **Check Query History**:
   Access previous queries to review or re-run documentation for updated resources.

## Future Improvements

- **Enhanced Compliance Checks**: Identify configurations that don't meet best practices or compliance standards.
- **Scheduled Documentation Updates**: Automatically document resources at scheduled intervals.
- **Interactive Query Suggestions**: Offer autocomplete suggestions based on common AWS documentation queries.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
