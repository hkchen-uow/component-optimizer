import argparse
import logging, logging.config
import opt_utils
# import opt_rest
# ide kell majd beraknom a saját programomat ami most pure néven szerepel

# az opt_rest fájlba viszont bele kell néznem, mert lehet, hogy ez egy egyszerű inicializálsá nem több

def launch_optimizer():
    args = parse_arguments()
    config = opt_utils.read_yaml(args.config_path)
    create_logger(config)
    # opt_utils.create_dirs(config.get('directories', ['data', 'log']).values())
    # opt_rest.init_service(config)
    # opt_rest.app.run(debug=True,
    #                  host=args.host,
    #                  port=args.port)
                     
def create_logger(config):
    try:
        logging.config.dictConfig(config.get('logging'))
        logger = logging.getLogger('optimizer')
    except Exception as e:
        print(f'ERROR: Cannot process configuration file: {e}')
    else:
        logger.info('Optimizer initialized successfully.')

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='MiCADO component to realize optimization of scaling decisions')
    parser.add_argument('--cfg',
                        dest='config_path',
                        default='./config/config.yaml',
                        help='path to configuration file')

    parser.add_argument('--host',
                        type=str,
                        default='127.0.0.1', # ezt át kell írnom az MTA gép lokális címére 192.168.0.60
                        help='host to bind service to')
    parser.add_argument('--port',
                        type=int,
                        default='5000',
                        help='port to bind service to')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    launch_optimizer()