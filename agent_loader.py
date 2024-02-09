import logging

def load_agent(config):
    try:
        module_name = config['agent_name'].lower() + "_agent"
        class_name = 'Agent'
        module = __import__(f"agents.{module_name}", fromlist=[class_name])
        agent = getattr(module, class_name)()
        if config['logging_enabled']:
            logging.info(f"Loaded agent {config['agent_name']}")
        return agent
    except (ImportError, AttributeError) as e:
        if config['logging_enabled']:
            logging.error(f"Error loading agent {config['agent_name']}: {e}")
        raise
