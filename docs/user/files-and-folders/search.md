---
sidebar_position: 70
id: search
title: Search
description: Using the search in OpenCloud
draft: false
---

# Using the search in OpenCloud

You can use the search bar in the top bar to find files and folders by their names, content, or assigned tags. A tag can match your search even when the search term does not appear in the file name or content.

## This is how the search works

- The search bar is located at the top of the top bar in the web interface.
  <img src={require("./img/search/searchbar.png").default} alt="Search bar" width="700"/>
- Shortcut: press `/` or type `s` to focus the search bar.
- Click on the drop-down menu next to the search bar.
- Select whether you want to search in all files or only in the current folder.
  <img src={require("./img/search/drop-down-menu-searchbar.png").default} alt="Select where to search" width="500"/>
- Enter a search term. Search checks file and folder names, file content, and assigned tags.
  <img src={require("./img/search/search-example.png").default} alt="Example search" width="700"/>

## Search using tags

Enter the name of an assigned tag in the search bar. Files and folders with that tag are included in the results, even if the tag name does not occur in their names or content.

## Filter search results by tags

- Open the complete search results.
- Open the tag filter to see the available tags.
- Select a tag to show only items with that tag.

<img src={require("./img/search/tag-filter-search-results.png").default} alt="Search results filtered by the important tag" width="1920"/>

## View matching search results

Search results show why an item matched:

- A matching tag is displayed below the result.
- For content matches, a matching text excerpt is displayed below the file name.
- Matching terms are highlighted in the excerpt.

<img src={require("./img/search/content-search-results.png").default} alt="Search results with matching text highlighted" width="1920"/>
