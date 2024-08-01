# Git state

- 디렉토리 구조

```
📦Chatbot_Pytorch
 ┣ 📂 .git
 ┃  ┣ 📜 config
 ┃  ┣ 📜 description
 ┃  ┣ 📜 HEAD
 ┃  ┣ 📜 hooks
 ┃  ┃  ┣ 📜 applypatch-msg.sample
 ┃  ┃  ┣ 📜 commit-msg.sample
 ┃  ┃  ┣ 📜 fsmonitor-watchman.sample
 ┃  ┃  ┣ 📜 post-update.sample
 ┃  ┃  ┣ 📜 pre-applypatch.sample
 ┃  ┃  ┣ 📜 pre-commit.sample
 ┃  ┃  ┣ 📜 pre-merge-commit.sample
 ┃  ┃  ┣ 📜 pre-push.sample
 ┃  ┃  ┣ 📜 pre-rebase.sample
 ┃  ┃  ┣ 📜 pre-receive.sample
 ┃  ┃  ┣ 📜 prepare-commit-msg.sample
 ┃  ┃  ┣ 📜 push-to-checkout.sample
 ┃  ┃  ┗ 📜 update.sample
 ┃  ┣ 📜 index
 ┃  ┣ 📜 info
 ┃  ┃  ┗ 📜 exclude
 ┃  ┣ 📜 logs
 ┃  ┃  ┣ 📜 HEAD
 ┃  ┃  ┗ 📜 refs
 ┃  ┃    ┣ 📜 heads
 ┃  ┃    ┃  ┣ 📜 dataset
 ┃  ┃    ┃  ┗ 📜 main
 ┃  ┃    ┗ 📜 remotes
 ┃  ┃      ┗ 📜 origin
 ┃  ┃        ┗ 📜 HEAD
 ┃  ┣ 📜 objects
 ┃  ┃  ┣ 📜 info
 ┃  ┃  ┗ 📜 pack
 ┃  ┃    ┣ 📜 pack-ec4cbf4b9c68450967ea8215c3fbaa2cd2c6b434.idx
 ┃  ┃    ┗ 📜 pack-ec4cbf4b9c68450967ea8215c3fbaa2cd2c6b434.pack
 ┃  ┣ 📜 packed-refs
 ┃  ┗ 📜 refs
 ┃    ┣ 📜 heads
 ┃    ┃  ┣ 📜 dataset
 ┃    ┃  ┗ 📜 main
 ┃    ┣ 📜 remotes
 ┃    ┃  ┗ 📜 origin
 ┃    ┃    ┗ 📜 HEAD
 ┃    ┗ 📜 tags
 ┣ 📜 .gitattributes
 ┣ 📜 .gitignore
 ┣ 📂 Batchfile
 ┃  ┣ 📜 venv_install.bat
 ┃  ┣ 📜 venv_install.sh
 ┃  ┣ 📜 venv_setup.bat
 ┃  ┗ 📜 venv_setup.sh
 ┣ 📂 Data_Processor
 ┃  ┣ 📜 filtered_daily_dialog
 ┃  ┃  ┣ 📜 dataset_dict.json
 ┃  ┃  ┣ 📜 test
 ┃  ┃  ┃  ┣ 📜 data-00000-of-00001.arrow
 ┃  ┃  ┃  ┣ 📜 dataset_info.json
 ┃  ┃  ┃  ┗ 📜 state.json
 ┃  ┃  ┣ 📜 train
 ┃  ┃  ┃  ┣ 📜 data-00000-of-00001.arrow
 ┃  ┃  ┃  ┣ 📜 dataset_info.json
 ┃  ┃  ┃  ┗ 📜 state.json
 ┃  ┃  ┗ 📜 validation
 ┃  ┃    ┣ 📜 data-00000-of-00001.arrow
 ┃  ┃    ┣ 📜 dataset_info.json
 ┃  ┃    ┗ 📜 state.json
 ┃  ┣ 📜 filtered_Dataset.py
 ┃  ┣ 📜 Json_processor
 ┃  ┃  ┣ 📜 flanT5_processor.py
 ┃  ┃  ┗ 📜 openai_Processor.py
 ┃  ┣ 📜 Origin_data
 ┃  ┃  ┣ 📜 csv
 ┃  ┃  ┃  ┣ 📜 test_li2017dailydialog.csv
 ┃  ┃  ┃  ┣ 📜 train_li2017dailydialog.csv
 ┃  ┃  ┃  ┗ 📜 validation_li2017dailydialog.csv
 ┃  ┃  ┣ 📜 CSV.py
 ┃  ┃  ┣ 📜 plt
 ┃  ┃  ┃  ┣ 📜 dialog_analysis.png
 ┃  ┃  ┃  ┗ 📜 dialog_analysis_distribution.png
 ┃  ┃  ┗ 📜 Plt.py
 ┃  ┣ 📜 Preprocessing_data
 ┃  ┃  ┣ 📜 csv
 ┃  ┃  ┃  ┣ 📜 test_li2017dailydialog.csv
 ┃  ┃  ┃  ┣ 📜 train_li2017dailydialog.csv
 ┃  ┃  ┃  ┗ 📜 validation_li2017dailydialog.csv
 ┃  ┃  ┣ 📜 CSV.py
 ┃  ┃  ┣ 📜 plt
 ┃  ┃  ┃  ┣ 📜 dialog_analysis.png
 ┃  ┃  ┃  ┗ 📜 dialog_analysis_distribution.png
 ┃  ┃  ┗ 📜 Plt.py
 ┃  ┗ 📜 TEST_Dataset.py
 ┣ 📜 delete_model.py
 ┣ 📜 git_directory_state.py
 ┣ 📂 GPT
 ┃  ┣ 📜 AI_gpt2.py
 ┃  ┣ 📜 AI_Response.py
 ┃  ┣ 📜 AI_TXT_Response.py
 ┃  ┗ 📜 model_pytorch
 ┃    ┣ 📜 chatbot_model.pth
 ┃    ┗ 📜 text_classifier.pth
 ┣ 📂 New_Data_Processor
 ┃  ┣ 📜 DataSet_Token_len.py
 ┃  ┗ 📜 excel
 ┃    ┣ 📜 dataset_extreme_value.xlsx
 ┃    ┗ 📜 dataset_lengths.xlsx
 ┣ 📜 README.md
 ┣ 📂 reddit
 ┃  ┣ 📜 data
 ┃  ┃  ┣ 📜 model_flan_t5_responses.json
 ┃  ┃  ┣ 📜 model_openai_responses.json
 ┃  ┃  ┣ 📜 processed_reddit_data.json
 ┃  ┃  ┣ 📜 reddit_data.json
 ┃  ┃  ┗ 📜 reddit_data.txt
 ┃  ┣ 📜 data_dialog
 ┃  ┃  ┗ 📜 reddit_data.json
 ┃  ┣ 📜 reddit_Scraper_Popular.py
 ┃  ┣ 📜 reddit_Scraper_Q&As.py
 ┃  ┣ 📜 reddit_Scraper_Q&As_1_1.py
 ┃  ┗ 📜 reddit_txt_Preprocessor.py
 ┣ 📜 requirements.txt
 ┗ 📂 Training
   ┣ 📜 new_train
   ┃  ┣ 📜 j5ng_TEST.py
   ┃  ┣ 📜 prompt_template.json
   ┃  ┣ 📜 T5_Trainer.py
   ┃  ┣ 📜 TreeNut_TEST.py
   ┃  ┣ 📜 TreeNut_Trainer.py
   ┃  ┗ 📜 __init__.py
   ┗ 📜 old_train
     ┣ 📜 Dialog.py
     ┣ 📜 Question-Answer.py
     ┣ 📜 seq2seq.py
     ┗ 📜 TextClassifier.py
```

- 변경 사항

```
✅ New_Data_Processor/DataSet_Token_len.py (추가)
❌ Training/Dialog.py (삭제)
❌ Training/Question-Answer.py (삭제)
❌ Training/TextClassifier.py (삭제)
✅ Training/new_train/T5_Trainer.py (추가)
✅ Training/new_train/TreeNut_Trainer.py (추가)
✅ Training/old_train/Dialog.py (추가)
✅ Training/old_train/Question-Answer.py (추가)
✅ Training/old_train/TextClassifier.py (추가)
✅ Training/old_train/seq2seq.py (추가)
❌ Training/seq2seq.py (삭제)
🔄 requirements.txt (수정)
```

