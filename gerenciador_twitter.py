import tweepy


class GerenciadorTwitter:
    @staticmethod
    def postar(nome_arquivo: str, frase_do_dia: str, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(consumer_key,
                                        consumer_secret,
                                        access_token,
                                        access_token_secret
                                        )

        api = tweepy.API(auth)
        pato_do_dia = api.media_upload(nome_arquivo)

        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

        create1 = client.create_tweet(media_ids=[pato_do_dia.media_id], text=frase_do_dia)
        print(create1)