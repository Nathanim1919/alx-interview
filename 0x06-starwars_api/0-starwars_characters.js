#!/usr/bin/node
const process = require('process');
const request = require('request');
const util = require('util');

// Promisify the request method
const requestPromise = util.promisify(request);

const printCharactersOfStarWarMovie = async () => {
    const movieId = process.argv[2];
    const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

    try {
        const response = await requestPromise(baseUrl);
        const movie = JSON.parse(response.body);

        for (let url of movie.characters) {
            const character = await requestPromise(url);
            console.log(JSON.parse(character.body).name);
        }
    } catch (error) {
        console.error(error);
    }
};

printCharactersOfStarWarMovie();
