# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: Python_Foundations
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: lesson_3a
 * Date: 10/4/15
 * Time: 8:26 PM
 * To change this template use File | Settings | File Templates.
"""
import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Constructor for Movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self, ):
        """

        Args:

        Returns:

        """
        webbrowser.open(self.trailer_youtube_url)
