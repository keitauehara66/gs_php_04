# gs_php_04
# 課題内容（どんな作品か）

- Python(Django)を使ったログインページ（CRUD）＋メインコンテンツ（文字列置換フォーム）<br>
  ・ログインページ：　画面上部にサインアップとログインボタン、ログインはメールアドレス、パスワードを使用（下記のテストアカウントが使用可能）<br>
  ・ログイン後メインページ：　画面上部にプロフィール（属性情報変更）とログアウトボタン、メインコンテンツも利用可能<br>

# DEMO
- HEROKUにデプロイ<br>
  https://gs-django-prac.herokuapp.com/

- テスアカウント<br>
  メールアドレス： test@test.com<br>
  パスワード： test12345678

- 注意点<br>
  サインアップを試す際は、パスワードは英数10桁以上での登録が必要

# 工夫した点・こだわった点

- 前回Djangoで作成したログインページに、メインコンテンツを追加<br>
- メインコンテンツはDBと接続しておらず、ログインして利用する程の内容ではないが、ログインしないと使えない仕様<br>
- DjangoアプリをHerokuにデプロイするために色々と追加で設定<br>
 
# Note

- Djangoについて<br>
  DjangoのModel-Template-Viewの構成はなんとなく分かってきた<br>
  一方、認証機能のパッケージ1つとっても、チューニングしようとするとどこで設定したら良いかがまだまだ読み解けない、コードの場所が分かってもいじり方がわからないなど、まだまだ壁は高い
- Gitについて<br>
  HEROKUにデプロイするのに何度かエラーを起こし、その際にコミットが増えていき、その所為かGithubにプッシュする際にもエラーを繰り返した<br>
  どのファイルは上げる必要があり、どのファイルは上げなくて良いなどの判断もよく分かっていない点があり引き続き勉強が必要

# Reference

- フルスタックチャンネル<br>
  Djangoカスタムユーザー構築チュートリアル レッスン1-3<br>
  https://www.youtube.com/watch?v=bM4_NSkcS-Y&list=PLoSZs76tLtJhKgmxYS9rpRrmWlOFVk2Hk&index=1

- 本堂俊輔のITエンジニアチャンネル<br>
  djangoフォームを自由自在に操ろう！ | djangoチュートリアル #8<br>
  https://www.youtube.com/watch?v=0WIoJor2Hhg

- DjangoアプリをHerokuにデプロイする方法<br>
  https://qiita.com/frosty/items/66f5dff8fc723387108c

