movies={
    'Mary': {'Big':
                {
                    'Watched': 1,
                    'Rating': 'G'
                },
             'Superman':
                {
                    'Watched': 3,
                    'Rating': 'PG'
                },
             "Finding Nemo":
                {
                    'Watched': 3,
                    'Rating': 'G'
                }
            },
    'Frank': {'Black Panther':
                {
                    'Watched': 1,
                    'Rating': 'PG-13'
                },
              'Kung Fu Panda':
                {
                    'Watched': 5,
                    'Rating': 'G'
                },
              'Pulp Fiction':
                {
                    'Watched': 1,
                    'Rating': 'R'
                }
             }
       }

print("Welcome to the Movie Lover's Club!!")
def main():
    print('1. Display all members')
    print('2. Display all movie information for a member')
    print('3. Increment the times a specific movie was watched by a member')
    print('4. Add a movie for a member')
    print('5. Add a new member')
    print('6. Remove a member')
    print('Q. Quit\n')
def member():
    print("Movie Lover's Club Members\n")
    print('=' * 33)
    for name in movies:
        print(name)

def moviez():
    name=input('Enter a name of a team member:')
    if name not in movies:
        print('This name does not appear in my database.\nPlease select option 5 to add a new member.')
    else:
        print("Movie Lover's Club Movies: {}\n".format(name))
        print('{:<15}{:>10}{:>7}'.format('Movies','Watched','Rating'))
        print('=' * 35)
        for namemovie in movies[name]:
            print('{:<15}{:>10}{:>7}'.format(namemovie, movies[name][namemovie]['Watched'],movies[name][namemovie]['Rating']))
def newmember():
    while True:
        add_member = input('Would you like to be added to the Club (Y/N)?').strip().upper()
        if add_member not in ['Y','N']:
            print('Invalid Entry: Please try again.')
        elif add_member == 'N':
            break
        else:
            name = input('Enter your name:')
            movies[name]={}
            print('{}, you have been added.'.format(name))
            break
def increment():
    name=input('Enter the name of a member:')
    if name not in movies:
        print('This name does not appear in my database.\nPlease select Option 5 to add a member.')

    else:
        namemovie =input('Enter the name of a movie:')
        if namemovie not in movies[name]:
            print('Sorry, I cant find this title.\nPlease select option 4 to add a movie.')
        else:
            watched=int(input('How many more times has time movie been watched?'))
            movies[name][namemovie]['Watched']=movies[name][namemovie]['Watched']+watched
            # print(movies[name][namemovie]['Watched'])
            print('Watch Time Increment:\n{} has now been watched {} times.'.format(namemovie,movies[name][namemovie]['Watched']))

def Exit():
    print('Goodbye')
def add_movie():
    name=input('Enter the name of a member.')
    if name not in movies:
        print('This name does not appear in my database.\nPlease select Option 5 to add a member.')
    else:
        movie_name = input('Enter the name of a movie.')
        if movie_name in movies[name]:
            print('That movie is already in this library.')
        else:
            movie_rating=input('Enter the rating of the movie.').strip().upper()
            times_watched=int(input('How many times has this movie been watched?'))
            movie = {movie_name: {"Watched": times_watched, "Rating": movie_rating}}
            movies[name].update(movie)
            print()
            print("Movie Lover's Club Movies: {}\n".format(name))
            print('{:<15}{:>10}{:>7}'.format('Movies', 'Watched', 'Rating'))
            print('=' * 35)
            for namemovie in movies[name]:
                   print('{:<15}{:>10}{:>7}'.format(namemovie, movies[name][namemovie]['Watched'],movies[name][namemovie]['Rating']))
def remove_member():
    name=input('Enter the name of the member you want to remove.')
    if name not in movies:
        print('That name is not in the database')
    else:
        del movies[name]
        print("{} has been removed from the Movie Lover's Club.".format(name))
while True:
    main()
    club_choices=['1','2','3','4','5','6','Q']
    choices = input('Please make a selection.').strip().upper()
    if choices not in club_choices:
        choices=input('Invalid Entry: Please Try again.')
    if choices in club_choices:
        if choices == '1':
            member()
            print()
            continue
        if choices == '2':
            moviez()
            print()
            continue
        if choices =='3':
            increment()
            print()
            continue
        if choices == '4':
            add_movie()
            print()
            continue
        if choices == '5':
            newmember()
            print()
            continue
        if choices == '6':
            remove_member()
            print()
            continue
        if choices in ['Q','Q']:
            Exit()
            print()
            break
print("Thank You for using the Movie Lover's Club!!!")

