#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define TEAM_N 30
#define TEAM_NAME_N 30+10
#define TOUR_NAME_N 100+10
#define CompRN 1000
#define SCORE_N 3

typedef struct {
  char name[TEAM_NAME_N];
  int points;
  int wins;
  int tie;
  int loss;
  int times;
  int score;
  int against;
}TS;

char teams[TEAM_N][TEAM_NAME_N];
char compResult[CompRN];
TS teamScore[TEAM_N];

int compare (const void *_a, const void *_b) {
  TS *a = (TS *)_a;
  TS *b = (TS *)_b;
  char ta[TEAM_NAME_N], tb[TEAM_NAME_N];
  int i, j;

  if (a->points < b->points) return -1;
  if (a->points > b->points) return 1;

  if (a->wins < b->wins) return -1;
  if (a->wins > b->wins) return 1;

  if ( (a->score-a->against) < (b->score-b->against) ) return -1;
  if ( (a->score-a->against) > (b->score-b->against) ) return 1;

  if (a->score < b->score) return -1;
  if (a->score > b->score) return 1;

  if (a->times > b->times) return -1;
  if (a->times < b->times) return 1;

  i = j = 0;
  while (a->name[i] != '\n') { ta[i] = tolower(a->name[i]); ++i; }
  ta[i] = '\0';
  while (b->name[j] != '\n') { tb[j] = tolower(b->name[j]); ++j; }
  tb[j] = '\0';

  return -1*strcmp (ta, tb);
}

int reverse (const void *_a, const void *_b) {
  return -1 * compare(_a, _b);
}

void parseResult(char *result, char *teamS, char *teamT, int *scoreS, int *scoreT) {
  int i, j;
  char score[SCORE_N];

  /* get teamS */
  j = 0;
  for (i=0; result[i]!='#'; i++)
    teamS[j++] = result[i];
  teamS[j++] = '\n';
  teamS[j] = '\0';

  /* get ScoreS */
  j = 0;
  for (i=i+1; result[i]!='@'; i++)
    score[j++] = result[i];
  score[j] = '\0';
  sscanf (score, "%d", scoreS);

  /* get ScoreT */
  j = 0;
  for (i=i+1; result[i]!='#'; i++)
    score[j++] = result[i];
  score[j] = '\0';
  sscanf (score, "%d", scoreT);

  /* get teamT */
  j = 0;
  for (i=i+1; result[i]!='\n'; i++)
    teamT[j++] = result[i];
  teamT[j++] = '\n';
  teamT[j] = '\0';
}

TS * findTeam (TS *teamScore, int n, char *name) {
  int i;
  for (i=0; i<n; i++)
    if (!strcmp(teamScore[i].name, name)) return &teamScore[i];

  return NULL;
}

int main() {
  int n, t, g;
  int i, j, k;
  int step;
  char tourName[TOUR_NAME_N];
  char teamS[TEAM_NAME_N], teamT[TEAM_NAME_N];
  int scoreS, scoreT;
  TS * curTeam;
  int nameLen;

  scanf ("%d\n", &n);
  for (step=0; step<n; step++) {
    /* get tourname */
    memset (tourName, 0, sizeof(tourName));
    fgets (tourName, TOUR_NAME_N, stdin);
    printf ("%s", tourName);

    /* get team name */
    memset (teams, 0, sizeof(tourName));
    scanf ("%d\n", &t);
    for (j=0; j<t; j++)
      fgets (teams[j], TEAM_NAME_N, stdin);

    /* init teamScore */
    memset (teamScore, 0, sizeof(teamScore));
    for (j=0; j<t; j++) {
      strcpy (teamScore[j].name, teams[j]);
      teamScore[j].points = teamScore[j].times = 0;
      teamScore[j].wins = teamScore[j].loss = teamScore[j].tie = 0;
      teamScore[j].score = teamScore[j].against = 0;
    }

    /* get comp result */
    scanf ("%d\n", &g);
    for (k=0; k<g; k++) {
      memset (compResult, 0, sizeof(compResult));
      fgets (compResult, sizeof(compResult), stdin);
      parseResult (compResult, teamS, teamT, &scoreS, &scoreT); 

      /* update scores */
      curTeam = findTeam (teamScore, t, teamS);
      curTeam->times ++;
      curTeam->score += scoreS;
      curTeam->against += scoreT;
      if (scoreS > scoreT) { curTeam->points += 3; curTeam->wins += 1; }
      if (scoreS < scoreT) { curTeam->loss += 1; }
      if (scoreS == scoreT) { curTeam->points += 1; curTeam->tie += 1; }

      curTeam = findTeam (teamScore, t, teamT);
      curTeam->times ++;
      curTeam->score += scoreT;
      curTeam->against += scoreS;
      if (scoreS < scoreT) { curTeam->points += 3; curTeam->wins += 1; }
      if (scoreS > scoreT) { curTeam->loss += 1; }
      if (scoreS == scoreT) { curTeam->points += 1; curTeam->tie += 1; }
    }

    qsort (teamScore, t, sizeof(teamScore[0]), reverse);

    for (i=0; i<t; i++) {
      nameLen = strlen(teamScore[i].name);
      teamScore[i].name[nameLen-1] = '\0';
      printf ("%d) %s %dp, %dg (%d-%d-%d), %dgd (%d-%d)\n", \
          (i+1), teamScore[i].name, teamScore[i].points, \
          teamScore[i].times, \
          teamScore[i].wins, teamScore[i].tie, teamScore[i].loss, \
          teamScore[i].score-teamScore[i].against, \
          teamScore[i].score, teamScore[i].against \
          );
    }
    if (step!=(n-1))printf ("\n");
  }

  return 0;
}
