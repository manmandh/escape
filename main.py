import logging
logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

try:

    import project.control as control

    def main():
        controller = control.ApplicationController()
        controller.run()


    if __name__ == "__main__":
        main()

except Exception as e:
    logging.exception("caught at main")
    raise e 
