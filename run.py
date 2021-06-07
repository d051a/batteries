from log_parser import log_data
from excel_parser import get_measured_ma
from excel_report_creator import creator

MEASURED_MA = get_measured_ma()


def get_batteries_count(log_entries):
    first_log_entry = log_entries[0]
    batteries_count = len(first_log_entry['mv'])
    return batteries_count


def get_battery_ma(log_entry, battery_id):
    battery_ma = log_entry['mv'][battery_id]
    return battery_ma


def get_battery_hours_delta(first_entry, second_entry):
    first_entry_time = first_entry['time']
    second_entry_time = second_entry['time']
    time_delta = second_entry_time - first_entry_time
    hours = float(time_delta.total_seconds()/60/60)
    return hours


def get_mv_average(mv_entries_list):
    mv_average = sum(mv_entries_list) / len(mv_entries_list)
    # mv_average = '{:.3f}'.format(mv_average/1000)
    return mv_average


def main():
    log_entries = list(log_data().values())
    first_entry = log_entries[0]
    batteries_count_on_stand = get_batteries_count(log_entries)
    batteies_results = {}
    for battery_id in range(batteries_count_on_stand):
        mv_entries = []
        for log_entry in log_entries:
            battery_ma = get_battery_ma(log_entry, battery_id)
            mv_entries.append(battery_ma)
            if battery_ma <= 2200:
                elapsed_time = get_battery_hours_delta(first_entry, log_entry)
                capacity_battery = MEASURED_MA * elapsed_time
                mv_average = get_mv_average(mv_entries)
                batteies_results.setdefault(battery_id, {'elapsed_time': None,
                                                         'capacity_battery': None,
                                                         'mv_average': None})
                batteies_results[battery_id]['elapsed_time'] = elapsed_time
                batteies_results[battery_id]['capacity_battery'] = capacity_battery
                batteies_results[battery_id]['mv_average'] = mv_average
                mv_entries.clear()
                break
    creator(batteies_results)


if __name__ == '__main__':
    main()