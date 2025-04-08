import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.lower().startswith("/help"):
        await message.channel.send("Çevre kirliliği hakkında sorular sorabilirsin.")
    if message.content.lower().startswith("çevre kirliliğinin zararları "):
        await message.channel.send("enerji kıtlığı,beslenme sorunları, canlı çeşitliliğinin azalması, toprakların kaybı, sağlık problemleri de gelişerek canlı yaşamının devamlılğını tehdit eder.")
    elif message.content.lower().startswith("çevre kirliliğinin sebepleri ") :
        await message.channel.send("Çevre kirliliğinin birçok sebebi vardır ve bunların çoğu insan faaliyetlerinden kaynaklanır. Sanayileşme, çevre kirliliğinin en büyük nedenlerinden biridir. Fabrikalar havaya, suya ve toprağa zararlı kimyasal maddeler bırakır. Sanayi tesislerinden çıkan zehirli gazlar hava kirliliğine sebep olurken, fabrika atıkları su kaynaklarını kirletir.")
    elif message.content.lower().startswith("çevre kirliliğini ") :
        await message.channel.send("Çevre kirliliğini önlemek için bireysel ve toplumsal düzeyde birçok önlem alınabilir. En etkili yöntemlerden biri, geri dönüşüm ve atık yönetimini doğru şekilde uygulamaktır. Plastik, cam, kağıt ve metal gibi atıklar ayrıştırılarak geri dönüştürülmelidir. Böylece hem doğaya atık bırakılmamış olur hem de doğal kaynaklar korunur.")
    elif message.content.lower().startswith("Çevre kirliliği ne"):
        await message.channel.send("Çevrenin hava, su ve toprak gibi unsurlarının zararlı maddelerle kirlenmesidir.")
    elif message.content.lower().startswith("Çevre kirliliği hangi "):
        await message.channel.send("Hava, su, toprak, ışık, ses (gürültü) ve radyoaktif kirlilik gibi türlere ayrılır.")
    elif message.content.lower().startswith("Hava kirliliğinin başlıca"):
        await message.channel.send("Fabrika gazları, araç egzozları, fosil yakıt kullanımı ve orman yangınları.")
    elif message.content.lower().startswith("Su kirliliğine neden olan"):
        await message.channel.send("Fabrika atıkları, kanalizasyon suları, tarımsal ilaçlar ve plastik atıklar.")
    elif message.content.lower().startswith("Toprak kirliliğine"):
        await message.channel.send("Kimyasal gübreler, sanayi atıkları ve plastik atıkların toprağa karışmasıyla oluşur.")
    elif message.content.lower().startswith("Gürültü kirliliği neden zararlıdır"):
        await message.channel.send("İnsanlarda stres, işitme kaybı ve uyku bozukluklarına neden olabilir.")
    elif message.content.lower().startswith("Işık kirliliğinin etkileri"):
        await message.channel.send("Gece gökyüzünün görünmesini engeller ve ekosistemleri olumsuz etkiler.")
    elif message.content.lower().startswith("Çevre kirliliği insan sağlığın"):
        await message.channel.send("Solunum yolu hastalıkları, su kaynaklı hastalıklar ve stres gibi sorunlara yol açar.")
    elif message.content.lower().startswith("Plastik atıklar neden büyük bir"):
        await message.channel.send("Uzun yıllar doğada çözünmez ve deniz canlılarına zarar verir.")
    

client.run("token")
