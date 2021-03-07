import calendar
from datetime import date, timedelta


# Tasks remaining:
# Create event implementation

def find_start_day(day, date_num):
	for i in range(date_num, 1, -1):
		if day > 0:
			day = day - 1
		else:
			day = 6
	return day


def find_end_day(day, date_num, month):
	month_length = find_month_length(month)

	for i in range(date_num, month_length):
		if day < 6:
			day = day + 1
		else:
			day = 0

	return day


def find_month_length(month):
	long_months = ["January", "March", "May", "July", "August", "October", "December"]
	short_months = ["April", "June", "September", "November"]

	if any(month in s for s in long_months):
		month_length = 31
	elif any(month in s for s in short_months):
		month_length = 30
	else:
		month_length = 28

	return month_length


def create_calendar():
	# Gets the date as an integer, the day of the week as a number between 0 and 6 and the month as a string
	current_date = date.today()
	current_date_num = current_date.day
	day = date.weekday(current_date)
	month = calendar.month_name[current_date.month]

	# Finds out what day of the week the month starts on
	start_day = find_start_day(day, current_date_num)
	end_day = find_end_day(day, current_date_num, month)

	days = []

	# Adds the month name and days of the week
	days.append(create_calendar_month(month))

	# Finds out what the previous month is and gets its length
	prev_month = calendar.month_name[(date.today().replace(day=1) - timedelta(days=1)).month]
	prev_month_length = find_month_length(prev_month)

	# Gets the date of the first day to be added from the previous month
	prev_month_days = prev_month_length - start_day + 1

	# Loops until the day of the week the month starts on adding days from the previous month
	for i in range(0, start_day):
		if (i - 1) % 7 == 0:
			days.append('<ul class="days">')

		days.append(create_calendar_other_day(prev_month_days))
		prev_month_days = prev_month_days + 1

	# Calculates the length of the current month
	month_length = find_month_length(month)

	# Adds the days of the current month to the calendar
	for i in range(1, month_length + 1):
		if (i - 1) % 7 == 0:
			days.append('<ul class="days">')

		days.append(create_calendar_day(i))

	# Loops until the day of the week the month ends on adding days from the next month
	for i in range(1, 7 - end_day):
		if (i - 1) % 7 == 0:
			days.append('<ul class="days">')

		days.append(create_calendar_other_day(i))

	return days


def create_calendar_month(month):
	return '<header> <h1>' + month + ' 2021</h1> </header> <div id="calendar"> <ul class="weekdays"> <li>Monday</li> <li>Tuesday</li> <li>Wednesday</li> <li>Thursday</li> <li>Friday</li> <li>Saturday</li> <li>Sunday</li> </ul>'


def create_calendar_other_day(day):
	return '<li class=\"day other-month\"> <div class=\"date\"> ' + str(day) + ' </div> </li>'


def create_calendar_day(day):
	return '<li class=\"day\"> <div class=\"date\">' + str(day) + '</div> </li>'


# Calendar base code for reference:
"""
    <li class="day">
                        <div class="date">1</div>
                    </li>
                    <li class="day">q

                        <div class="date">2</div>
                        <div class="event">
                            <div class="event-desc">
                                Career development @ Community College room #402
                            </div>
                            <div class="event-time">
                                2:00pm to 5:00pm
                            </div>
                        </div>
                    </li>
                </ul>
          <ul class="days">
                    <li class="day">
                        <div class="date">3</div>
                    </li>
                    <li class="day">
                        <div class="date">4</div>
                    </li>
                    <li class="day">
                        <div class="date">5</div>
                    </li>
                    <li class="day">
                        <div class="date">6</div>
                    </li>

            <!-- Row #2 -->

                    <li class="day">
                        <div class="date">7</div>
                        <div class="event">
                            <div class="event-desc">
                                Group Project meetup
                            </div>
                            <div class="event-time">
                                6:00pm to 8:30pm
                            </div>
                        </div>
                    </li>
                    <li class="day">
                        <div class="date">8</div>
                    </li>
                    <li class="day">
                        <div class="date">9</div>
                    </li>
                </ul>

                <ul class="days">
                    <li class="day">
                        <div class="date">10</div>
                    </li>
                    <li class="day">
                        <div class="date">11</div>
                    </li>
                    <li class="day">
                        <div class="date">12</div>
                    </li>
                    <li class="day">
                        <div class="date">13</div>

            <!-- Row #3 -->

                    </li>
                    <li class="day">
                        <div class="date">14</div><div class="event">
                            <div class="event-desc">
                                Board Meeting
                            </div>
                            <div class="event-time">
                                1:00pm to 3:00pm
                            </div>
                        </div>
                    </li>
                    <li class="day">
                        <div class="date">15</div>
                    </li>
                    <li class="day">
                        <div class="date">16</div>
                    </li>
                </ul>

                <ul class="days">
                    <li class="day">
                        <div class="date">17</div>
                    </li>
                    <li class="day">
                        <div class="date">18</div>
                    </li>
                    <li class="day">
                        <div class="date">19</div>
                    </li>
                    <li class="day">
                        <div class="date">20</div>
              <!-- Row #4 -->

                    </li>
                    <li class="day">
                        <div class="date">21</div>
                    </li>
                    <li class="day">
                        <div class="date">22</div>
                        <div class="event">
                            <div class="event-desc">
                                Conference call
                            </div>
                            <div class="event-time">
                                9:00am to 12:00pm
                            </div>
                        </div>
                    </li>
                    <li class="day">
                        <div class="date">23</div>
                    </li>
                </ul>

                <ul class="days">
                    <li class="day">
                        <div class="date">24</div>
                    </li>
                    <li class="day">
                        <div class="date">25</div>
                        <div class="event">
                            <div class="event-desc">
                                Conference Call
                            </div>
                            <div class="event-time">
                                1:00pm to 3:00pm
                            </div>
                        </div>
                    </li>
                    <li class="day">
                        <div class="date">26</div>
                    </li>
                    <li class="day">
                        <div class="date">27</div>
              <!-- Row #5 -->

                    </li>
                    <li class="day">
                        <div class="date">28</div>
                    </li>
                    <li class="day other-month">
                        <div class="date">1</div>
                    </li>
                    <li class="day other-month">
                        <div class="date">2</div>
                    </li>
                </ul>

                <!-- Row #6 -->

                <ul class="days">
                    <li class="day other-month">
                        <div class="date">3</div>
                    </li>
                    <li class="day other-month">
                        <div class="date">4</div> <!-- Next Month -->
                    </li>
                    <li class="day other-month">
                        <div class="date">5</div>
                    </li>
                    <li class="day other-month">
                        <div class="date">6</div>
                    </li>
"""
