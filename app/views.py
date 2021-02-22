from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def login(request):
    return render(request, 'app/login.html')


def dashboard(request):
    calendar = create_calendar()
    tasks = {'tasks': Task.objects.all(),
             'calendar': calendar}
    # payments = {'payments': Payment.object.all()}
    return render(request, 'app/index.html', tasks)


def signup(request):
    return render(request, 'app/signup.html')


def forgot_password(request):
    return render(request, 'app/password.html')


def create_calendar():
    days = []
    for i in range(1, 31):
        if (i - 1) % 7 == 0:
            days.append('<ul class="days">')

        days.append(create_calendar_day(i))

    return days


def create_calendar_day(day):
    return '<li class=\"day\"> <div class=\"date\">' + str(day) + '</div> </li>'


# Calendar base code:
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
