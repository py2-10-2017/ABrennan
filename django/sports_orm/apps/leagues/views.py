from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseballs": League.objects.filter(sport__contains="baseball"),
		"womens": League.objects.filter(name__contains="women"),
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
		"atlanticsoccers": Team.objects.filter(league_id=League.objects.get(name="Atlantic Soccer Conference")),
		"penguins": Player.objects.filter(curr_team_id=Team.objects.get(team_name="Penguins")),
		"baseballconferences": Player.objects.filter(curr_team_id__league_id=League.objects.get(name="International Collegiate Baseball Conference")),
		"footballopezes": Player.objects.filter(curr_team_id__league_id=League.objects.get(name="American Conference of Amateur Football"), last_name="Lopez"),
		"footballers": Player.objects.filter(curr_team_id__league_id__sport="Football"),
		"sophiateams": Team.objects.filter(curr_players__first_name="Sophia"),
		"sophialeagues": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"floreses": Player.objects.filter(last_name="Flores").exclude(curr_team=Team.objects.filter(location="Washington")),
		"samuels": Team.objects.filter(all_players__first_name="Samuel")&Team.objects.filter(all_players__last_name="Evans"),
		"manitobas": Player.objects.filter(all_teams__location="Manitoba"),
		"vikings": Player.objects.filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita"),
		"grayteams": Team.objects.filter(all_players__last_name="Gray", all_players__first_name="Jacob").exclude(curr_players__last_name="Gray", curr_players__first_name="Jacob"),
		"joshuaatlantics": Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players",first_name="Joshua"),
		"twelves": Team.objects.annotate(player_count=Count('all_players')).filter(player_count__gt=12),
		"playerteams": Player.objects.annotate(player_count=Count('all_teams')).all().order_by("-player_count")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
