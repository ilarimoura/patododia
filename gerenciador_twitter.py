import tweepy


class GerenciadorTwitter:

    def __init__(self, dados_twitter):
        self.consumer_key = dados_twitter['consumer_key']
        self.consumer_secret = dados_twitter['consumer_secret']
        self.access_token = dados_twitter['access_token']
        self.access_token_secret = dados_twitter['access_token_secret']

    def postar(self, nome_arquivo: str, frase_do_dia: str):
        auth = tweepy.OAuth1UserHandler(self.consumer_key,
                                        self.consumer_secret,
                                        self.access_token,
                                        self.access_token_secret
                                        )

        api = tweepy.API(auth)
        pato_do_dia = api.media_upload(nome_arquivo)

        client = tweepy.Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

        create1 = client.create_tweet(media_ids=[pato_do_dia.media_id], text=frase_do_dia)
        print(create1)