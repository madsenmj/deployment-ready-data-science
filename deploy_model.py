


# Implement test code to run in IDE or Azure ML Workbench
if __name__ == '__main__':
    # Import the logger only for Workbench runs

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--retrain', action='store_true', help='Retrain Model')
    args = parser.parse_args()


    print("Common Init code here")

    if args.retrain:
        print("retrain model")
        print("...Retrain code here...")
    else:
        print("Default server run code here")