from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseballs": League.objects.filter(sport__contains="baseball"),
		"womens": League.objects.filter(name__contains='women'),
		"hockeys": League.objects.filter(sport__contains="hockey"),
		"nofootballs": League.objects.exclude(sport__contains="football"),
		"conferences": League.objects.filter(name__contains="conference"),
		"atlantics": League.objects.filter(name__contains="atlantic"),
		"dallases": Team.objects.filter(location__contains="dallas"),
		"raptors": Team.objects.filter(team_name__contains="raptor"),
		"cities": Team.objects.filter(location__contains="city"),
		"tees": Team.objects.filter(team_name__startswith="T"),
		"locations": Team.objects.all().order_by("location"),
		"alphabeticals": Team.objects.all().order_by("-team_name"),
		"coopers": Player.objects.filter(last_name__contains="cooper"),
		"joshuas": Player.objects.filter(first_name="Joshua"),
		"nojoshcoopers": Player.objects.filter(last_name__contains="cooper").exclude(first_name="Joshua"),
		"alexwyatts": Player.objects.filter(first_name__contains="alexander")|Player.objects.filter(first_name__contains="wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
