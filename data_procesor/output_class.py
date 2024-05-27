import json

from constans import emoji
from utilities.log_class import LogClass


class Output:
    log: LogClass
    flag: set()
    duplicated_hour_table_jason = {"Time_table": {}}

    def __init__(self, log):
        self.log = log

    def no_duplicates_final_output_to_list(self, time_table):
        final_output_list = []
        try:
            for hour in time_table:
                reformed_hour_table = []
                for minutes in hour[1]:
                    reformed_hour_table.append(f"{hour[0]}:{minutes}")
                final_output_list.append(reformed_hour_table)
        except Exception as e:
            self.log.critical(f"couldn't generate no duplicate list"
                              f" {emoji.TASK_FAILED}. Error: {e}")
        finally:
            return final_output_list

    def mixed_duplicates_final_output_to_json(self, time_table):
        no_duplicates = []
        for hour in time_table:
            if hour[0] in self.flag:
                self.duplicated_hour_table_jason["Time_table"][f"{hour[0]} hours"] = \
                    {f"Bus - {index} at minute": minute for index, minute
                     in enumerate(hour[1], start=1)}
            else:
                no_duplicates.append(hour)
        if no_duplicates:
            print(f"Without duplicates {emoji.TASK_SUCCSEEDED}:")
            print(self.no_duplicates_final_output_to_list(no_duplicates))
        self.print_to_jason_file()

    def print_to_jason_file(self):
        with open("json_file.json", mode="w", encoding='UTF-8') as json_file:
            json.dump(self.duplicated_hour_table_jason, json_file, indent=4)
            self.log.info(f"{emoji.INFO} output printed into json_file")

    def output_final_results(self, time_table, flag):
        self.flag = flag
        if not self.flag:
            print("no duplicates found. list: ")
            print(self.no_duplicates_final_output_to_list(time_table))
            self.log.info(f"{emoji.INFO}bus schedules happen to be without duplicates")
        else:
            print(f"{emoji.INFO}found {len(self.flag)} duplicates."
                  f" You can find them in json_file")
            self.mixed_duplicates_final_output_to_json(time_table)
            self.log.info(f"{emoji.INFO}found {len(self.flag)} duplicates. "
                          f"You can find them in json_file")
