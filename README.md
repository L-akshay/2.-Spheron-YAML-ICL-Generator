# 2.-Spheron-YAML-ICL-Generator

## Overview
The **Spheron YAML Generator** is a natural language-driven tool that simplifies the process of creating YAML configurations for Spheron's Infrastructure Composition Language (ICL). Developers can describe their service requirements in plain English, and the generator will produce a valid YAML file that adheres to Spheron's ICL specifications.

## Features
- **Natural Language Parsing**: Converts user input (e.g., *"I want a Node.js service with auto-scaling and 1 GB of memory"*) into structured YAML.
- **Validation & Error Prevention**: Ensures the generated YAML follows Spheron's ICL specifications to prevent misconfigurations.
- **Easy Iterations**: Users can refine the generated YAML by adjusting their natural language descriptions.
- **Interactive Interface**: A chat-like interface that allows developers to generate, modify, and validate YAML configurations in real-time.

## Installation
### Prerequisites
- Python 3.x
- `PyYAML` library

### Setup
Clone the repository and install dependencies:
```sh
git clone <repository_url>
cd spheron-yaml-generator
pip install -r requirements.txt
```

## Usage
Run the generator script:
```sh
python main.py
```
Then, enter your service description in natural language. Example:
```sh
Describe your service: I want a Node.js service with auto-scaling and 2 GB of memory.
```
The script will generate a YAML configuration based on the input and display it.

## Example Output
### User Input:
```
I want a Node.js service with auto-scaling and 2 GB of memory.
```
### Generated YAML:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-service
  template:
    metadata:
      labels:
        app: my-service
    spec:
      containers:
        - name: my-container
          image: node:latest
          resources:
            requests:
              memory: 2Gi
```

## Contributing
1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a pull request

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


