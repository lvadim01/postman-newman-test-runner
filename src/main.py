from runTests import RunTests
from models.emailObject import EmailObject
from service.argumentParser import ArgumentParser
from service.sendReportEmail import SendReportEmail
import sys, traceback


def main(env, collection_name, has_report):
    # run test suites
    suite = RunTests(env, collection_name)
    report_files = suite.run_tests()

    if has_report:
        try:
            # send report email
            email = EmailObject(
                files=report_files, env=env, collection=collection_name)
            SendReportEmail(email)
        except Exception:
            print "Error: Cannot send email"
            exit(1)

    print 'All good :-)'

if __name__ == "__main__":
    try:
        parser = ArgumentParser()
        args = parser.get_arguments()
    except Exception:
        print 'Error: Cannot parse arguments'
        exit(1)

    print "Program started with the following parameters:"
    print "Environment: " + args.environment
    print 'Collection: ' + args.collection
    print "Report recipients: " + args.report
    print "For more info - python main.py -h or --help"

    try:
        collection_list = args.collection
        collection = collection_list[1:-1]

        report = False
        if args.report == 'true':
            report = True

        main(args.environment, collection.split(','), report)

    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        print e
        print "Error: Bad arguments"
        exit(1)

