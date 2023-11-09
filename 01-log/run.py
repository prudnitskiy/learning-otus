#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
import argparse
import logging


def find_log():
    return True


def parse_log(path: str):
    return True


def parse_string(string: str):
    return True


def render_template():
    return True


if __name__ == "__main__":
    print("ok")
    argparser = argparse.ArgumentParser(description="Парсер для логов (ДЗ-1)")
    argparser.add_argument(
        '--verbose',
        '-v',
        help="verbosity level",
        default="info"
    )
    argparser.add_argument(
        "--path",
        "-p",
        help="path to logfile",
        required=True
    )
    argparser.add_argument(
        "--config",
        "-c",
        help="path to config"
    )

    clargs = argparser.parse_args()

    logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s',
                        level=clargs.verbose.upper())

    logging.info("запускаюсь")
    logging.info(f"путь к журналу для парсинга: {clargs.path}")

    report = []
    report_failed = 0
    report_all = 0

    log = find_log(clargs.path)
    for logstring in parse_log(log):
        report_all += 1
        try:
            report.append(parse_string(string=logstring))
        except ValueError:
            report_failed += 1

    if report_failed >= report_failed * 0.3:
        logging.info(f"{report_failed} из {report_all} не удалось прочитать. Изменение формата?")

    render_template(report)

