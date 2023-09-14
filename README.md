# git
...或在命令行上创建新的存储库
echo "# some-experience-when-use-git" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/HengYuh/some-experience-when-use-git.git
git push -u origin main



...或从命令行推送现有存储库
git remote add origin https://github.com/HengYuh/some-experience-when-use-git.git
git branch -M main
git push -u origin main


fatal: unable to access 'https://github.com/LinyangLee/BERT-Attack.git/': Recv failure: Connection was reset
$ git config --global --unset https.proxy   #may solve this problem

heng'ge@LAPTOP-NI1B9H83 MINGW64 /d/桌面/github (master)
$ git clone https://github.com/LinyangLee/BERT-Attack.git
Cloning into 'BERT-Attack'...
fatal: unable to access 'https://github.com/LinyangLee/BERT-Attack.git/': Recv failure: Connection was reset
        heng'ge@LAPTOP-NI1B9H83 MINGW64 /d/桌面/github (master)
        $ git config --global --unset https.proxy
        
        heng'ge@LAPTOP-NI1B9H83 MINGW64 /d/桌面/github (master)
        $ git clone https://github.com/LinyangLee/BERT-Attack.git
        Cloning into 'BERT-Attack'...
        remote: Enumerating objects: 9, done.
        remote: Counting objects: 100% (9/9), done.
        remote: Compressing objects: 100% (8/8), done.
        remote: Total 9 (delta 0), reused 9 (delta 0), pack-reused 0
        Receiving objects: 100% (9/9), 510.28 KiB | 303.00 KiB/s, done.
