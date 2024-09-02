# Python YouTube

An async implementation of Python API for YouTube Data V3 based on: [python-youtube](https://github.com/sns-sdks/python-youtube). Thanks a lot for the original developers 🙏

__NOTE__: It's a breaking fork. A lot of functionality has been removed or completely refactored. This fork doesn't support Media uploads, the old API client, `update`, `delete`, `insert` API operations. It only works with `dataclasses`. It is intended to be a performant and robust client to **retrieve** resources from the API only.

Compatible with Python 3.9+.

## Features

- Asynchronous API client to retrieve YouTube Data API resources.
- Built with `dataclasses` only. Minimal dependencies: `aiohttp` and `orjson`.

## Installation

Install the package directly from the repository:

```
rye add python-youtube --git https://github.com/Maekersuite/python-youtube --branch master
```

## Usage

### Client Initialization

You can initialize the client using either an API key or an access token:

```python
from pyyoutube import Client, APIKeyAuthentication

# Using API key
client = Client(APIKeyAuthentication(api_key='YOUR_API_KEY'))

# Using access token
client = Client(AccessTokenAuthentication(access_token='YOUR_ACCESS_TOKEN'))
```

### Retrieving Videos

To retrieve videos, you can use the `videos.list` method:

```python
videos = await client.videos.list(video_id'VIDEO_ID')
```

Some of the resources subgroups are encapsulated in their parent resource classes. For example, to retrieve `VideoCategories`, you need to use `client.video.categories.list()`.

```python
categories = await client.video.categories.list(region_code='US')
```

### Available Resources

The following resources are available:

- [Captions](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/captions.py)
- [Channel Sections](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/channel_sections.py)
- [Channels](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/channels.py)
- [Comment Threads](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/comment_threads.py)
- [Comments](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/comments.py)
- [I18n Languages](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/i18n_languages.py)
- [I18n Regions](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/i18n_regions.py)
- [Members](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/members.py)
- [Membership Levels](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/membership_levels.py)
- [Playlist Items](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/playlist_items.py)
- [Playlists](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/playlists.py)
- [Search](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/search.py)
- [Subscriptions](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/subscriptions.py)
- [Video Abuse Report Reasons](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/video_abuse_report_reasons.py)
- [Video Categories](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/video_categories.py)
- [Videos](https://github.com/Maekersuite/python-youtube/blob/master/pyyoutube/resources/videos.py)
