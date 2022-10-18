Instructions:

Make sure you have TMUX and go to your Github Repo > Settings > Webhooks > Add webhook and make sure it points to your API endpoint.

Select Content type: application/json, select just the push event and select as active.

Make sure the API is running on the background of your system via TMUX or similar.

Create one TMUX screen with the name "GitAccess" and open your local Github cloned folder on it.

Everytime the Github hook sents a successful request to your API, the push command will be automatically sent

--Only Works On UNIX Systems--
