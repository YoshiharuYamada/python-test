# パイソンの勉強

## バージョン管理

### インストール
```
 brew install pyenv
```
### 環境設定
```
$ cat << 'EOS' >> ~/.bash_profile
> export PYENV_ROOT=/usr/local/var/pyenv
> if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
> EOS
$ source ~/.bash_profile
```
### インストール可能なバージョン確認

```
pyenv install --list
```

### pythonのインストール

```
pyenv install 3.7.3
```

#### 失敗したら？

```
 $ vim ~/.bash_profile
 # 環境変数を追記
 export CFLAGS="-I$(brew --prefix readline)/include -I$(brew --prefix openssl)/include -I$(xcrun --show-sdk-path)/usr/include"
 export LDFLAGS="-L$(brew --prefix readline)/lib -L$(brew --prefix openssl)/lib"
 export PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs2"
 export PATH=$PATH:$HOME/.pyenv/shims
 $ source ~/.bash_profile
```

#### それでも失敗したら？Mojave用のmacOS SDK headerがデフォルトで入っていない
```
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

### インストール確認
```
pyenv versions
```

