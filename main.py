import os

from dotenv import load_dotenv
from utilities.base_class import Base


def main():
    for index in range(3):
        main_obj = Base(index)
        main_obj.landing_page.go_to_vvt_schedule()
        main_obj.schedule_page.select_4g()
        main_obj.schedule_page.select_europe_square_stop()
        main_obj.schedule_page.select_todays_schedule()
        main_obj.database_manipulating.create_database()
        main_obj.database_manipulating.create_database_table()
        main_obj.database_manipulating.input_data_into_database_table(
            main_obj.scraper.scraping_data())
        main_obj.output.output_final_results(
            main_obj.database_manipulating.get_data_from_database(),
            main_obj.database_manipulating.get_flag())
        main_obj.close()


def single_use(index):
    main_obj = Base(index)
    main_obj.landing_page.go_to_vvt_schedule()
    main_obj.schedule_page.select_4g()
    main_obj.schedule_page.select_europe_square_stop()
    main_obj.schedule_page.select_todays_schedule()
    main_obj.database_manipulating.create_database()
    main_obj.database_manipulating.create_database_table()
    main_obj.database_manipulating.input_data_into_database_table(
        main_obj.scraper.scraping_data())
    main_obj.output.output_final_results(
        main_obj.database_manipulating.get_data_from_database(),
        main_obj.database_manipulating.get_flag())
    main_obj.close()


def setup():
    try:
        os.remove("log_file.log")
    except Exception as e:
        print(f"Failed to restart log file. error: {e}")
        os.close()
    load_dotenv()


if __name__ == '__main__':
    setup()
    main()
    # single_use(1)
