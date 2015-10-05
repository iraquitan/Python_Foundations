# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: Python_Foundations
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: lesson_3a_entertainment_center
 * Date: 10/4/15
 * Time: 11:18 PM
 * To change this template use File | Settings | File Templates.
"""
import fresh_tomatoes
import lesson_3a_media

toy_story = lesson_3a_media.Movie('Toy Story', 'A story of a boy and his toys that come to life',
                                  'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                                  'https://www.youtube.com/watch?v=KYz2wyBy3kc')
# print(toy_story.storyline)

# avatar = lesson_3a_media.Movie('Avatar', 'A marine on an alien planet',
#                                'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
#                                'https://www.youtube.com/watch?v=5PSNL1qE6VY')
# print(avatar.storyline)
# avatar.show_trailer()
v_for_vendetta = lesson_3a_media.Movie('V for Vendetta',
                                       'Following world war, London is a police state occupied by a fascist government, and a vigilante known only as V (Hugo Weaving) uses terrorist tactics to fight the oppressors of the world in which he now lives.',
                                       'https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg',
                                       'https://www.youtube.com/watch?v=lSA7mAHolAw')

# school_of_rock = lesson_3a_media.Movie('School of Rock', 'Using rock music to learn',
#                                        'http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg',
#                                        'https://www.youtube.com/watch?v=3PsUJFEBC74')

# ratatouille = lesson_3a_media.Movie('Ratatouille', 'A rat is a chef in Paris',
#                                     'http://images.fanpop.com/images/image_uploads/Ratatouille-poster-ratatouille-324474_1215_1800.jpg',
#                                     'https://www.youtube.com/watch?v=niD-jahFURU')

# midnight_in_paris = lesson_3a_media.Movie('Midnight in Paris', 'Going back in time to meet authors',
#                                           'http://images.moviepostershop.com/midnight-in-paris-movie-poster-2011-1020695872.jpg',
#                                           'https://www.youtube.com/watch?v=FAfR8omt-CY')

# hunger_games = lesson_3a_media.Movie('Hunger Games', 'A really real reality show',
#                                      'http://www.movieguide.org/wp-content/uploads/2012/06/98068201-0cc9-42ed-81ee-dcd480c4cba8.jpg',
#                                      'https://www.youtube.com/watch?v=PbA63a7H0bo')

lotr_1 = lesson_3a_media.Movie('The Lord of The Rings - The Fellowship of the Ring', 'The story begins in the Shire, where the Hobbit Frodo Baggins inherits the Ring from Bilbo Baggins, his cousin and guardian.',
                                     'http://www.movieposter.com/posters/archive/main/105/MPW-52979',
                                     'https://www.youtube.com/watch?v=V75dMMIW2B4')

lotr_2 = lesson_3a_media.Movie('The Lord of The Rings - The Two Towers', 'Orcs sent by Saruman and Sauron kill Boromir and kidnap Merry and Pippin. After agonizing over which pair of hobbits to follow, Aragorn, Gimli and Legolas pursue the orcs bearing Merry and Pippin to Saruman.',
                                     'https://wtfbabe.files.wordpress.com/2012/11/two-towers-poster.jpg',
                                     'https://www.youtube.com/watch?v=LbfMDwc4azU')

lotr_3 = lesson_3a_media.Movie('The Lord of The Rings - The Return of the King', 'Sauron unleashes a heavy assault upon Gondor. Gandalf arrives at Minas Tirith to alert Denethor of the impending attack.',
                                     'http://sites.psu.edu/202d031/wp-content/uploads/sites/15365/2014/09/LOTR-King.jpg',
                                     'https://www.youtube.com/watch?v=r5X-hFf6Bwo')

matrix = lesson_3a_media.Movie('The Matrix', 'Neo (Keanu Reeves) believes that Morpheus (Laurence Fishburne), an elusive figure considered to be the most dangerous man alive, can answer his question -- What is the Matrix? Neo is contacted by Trinity (Carrie-Anne Moss), a beautiful stranger who leads him into an underworld where he meets Morpheus. They fight a brutal battle for their lives against a cadre of viciously intelligent secret agents. It is a truth that could cost Neo something more precious than his life.',
                                     'https://www.movieposter.com/posters/archive/main/9/A70-4902',
                                     'https://www.youtube.com/watch?v=vKQi3bBA1y8')

# movies = [toy_story, avatar, v_for_vendetta, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
movies = [toy_story, v_for_vendetta, lotr_1, lotr_2, lotr_3, matrix]
fresh_tomatoes.open_movies_page(movies)
