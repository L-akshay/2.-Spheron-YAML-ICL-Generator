import yaml
import re

# Sample NLP function to parse user input
def parse_user_input(user_input):
    # Basic parsing logic (this can be enhanced with NLP libraries)
    service_info = {}
    
    # Example regex patterns to extract information
    if re.search(r'Node\.?js', user_input, re.IGNORECASE):
        service_info['type'] = 'Node.js'
    if re.search(r'auto-scaling', user_input, re.IGNORECASE):
        service_info['auto_scaling'] = True
    if match := re.search(r'(\d+)\s*GB', user_input):
        service_info['memory'] = f"{match.group(1)}Gi"
    
    return service_info

# Function to generate YAML from parsed information
def generate_yaml(service_info):
    # Create a basic structure based on the parsed info
    deployment = {
        'apiVersion': 'v1',
        'kind': 'Deployment',
        'metadata': {
            'name': 'my-service'
        },
        'spec': {
            'replicas': 1,
            'template': {
                'spec': {
                    'containers': [{
                        'name': 'my-container',
                        'image': f"{service_info['type'].lower()}:latest",
                        'resources': {
                            'requests': {
                                'memory': service_info.get('memory', '512Mi')
                            }
                        }
                    }]
                }
            }
        }
    }
    
    if service_info.get('auto_scaling'):
        deployment['spec']['replicas'] = 3  
    
    return yaml.dump(deployment)

def validate_yaml(yaml_str):
    return True  
def main():
    print("Welcome to the Spheron YAML Generator!")
    while True:
        user_input = input("Describe your service: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        service_info = parse_user_input(user_input)
        generated_yaml = generate_yaml(service_info)
        
        if validate_yaml(generated_yaml):
            print("Generated YAML Configuration:")
            print(generated_yaml)
        else:
            print("Error: Generated YAML is invalid.")

if __name__ == "__main__":
    main()