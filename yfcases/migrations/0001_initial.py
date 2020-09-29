# Generated by Django 3.1 on 2020-09-18 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'yfcase_city',
            },
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yfcases.city')),
            ],
            options={
                'db_table': 'yfcase_township',
            },
        ),
        migrations.CreateModel(
            name='Yfcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yfcaseCaseNumber', models.CharField(max_length=100, verbose_name='案號(*)')),
                ('yfcaseCompany', models.CharField(blank=True, max_length=50, null=True, verbose_name='所屬公司')),
                ('yfcaseBigSection', models.CharField(blank=True, max_length=10, null=True, verbose_name='段號')),
                ('yfcaseSmallSection', models.CharField(blank=True, max_length=10, null=True, verbose_name='小段')),
                ('yfcaseOtherAddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='其他住址')),
                ('yfcaseDebtor', models.CharField(blank=True, max_length=10, null=True, verbose_name='債務人')),
                ('yfcaseCreditor', models.CharField(blank=True, max_length=10, null=True, verbose_name='債權人')),
                ('yfcaseCity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yfcases.city')),
                ('yfcaseTownship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yfcases.township')),
            ],
            options={
                'db_table': 'yfcase_yfcase',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyFirstDay', models.CharField(blank=True, max_length=100, null=True, verbose_name='初勘日')),
                ('surveySecondDay', models.CharField(blank=True, max_length=100, null=True, verbose_name='會勘日')),
                ('surveyForeclosureAnnouncementLink', models.URLField(blank=True, null=True, verbose_name='法拍公告(證物三)')),
                ('survey988Link', models.URLField(blank=True, null=True, verbose_name='998連結')),
                ('surveyObjectPhotoLink', models.URLField(blank=True, null=True, verbose_name='物件照片(證物四)')),
                ('surveyNetMarketPriceLink', models.URLField(blank=True, null=True)),
                ('surveyForeclosureRecordLink', models.URLField(blank=True, null=True, verbose_name='法拍記錄(證物七)')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectBuildAddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('objectBuildTotalPrice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='總價(NT)')),
                ('objectBuildBuildArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='建坪(坪)')),
                ('objectBuildHouseAge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='屋齡(年)')),
                ('objectBuildFloorHeight', models.CharField(blank=True, max_length=100, null=True, verbose_name='樓高')),
                ('objectBuildStatus', models.CharField(blank=True, max_length=100, null=True, verbose_name='狀態')),
                ('objectBuildTransactionDate', models.CharField(blank=True, max_length=100, null=True, verbose_name='成交日期')),
                ('objectBuildUrl', models.URLField(blank=True, null=True, verbose_name='附件')),
                ('objectBuildScorerA', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員A')),
                ('objectBuildScorerB', models.CharField(blank=True, max_length=100, null=True, verbose_name='勘查員B')),
                ('objectBuildScorRateA', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成A')),
                ('objectBuildScorRateB', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='加成B')),
                ('objectBuildScorReasonA', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因A')),
                ('objectBuildScorReasonB', models.CharField(blank=True, max_length=100, null=True, verbose_name='加成原因B')),
                ('plusItemA1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemA5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherA', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueA1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueA5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherA', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusItemB1', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB2', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB3', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB4', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemB5', models.CharField(blank=True, max_length=100, null=True)),
                ('plusItemOtherB', models.CharField(blank=True, max_length=100, null=True)),
                ('plusValueB1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueB5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('plusValueOtherB', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True)),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectbuilds', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='地號')),
                ('landUrl', models.URLField(blank=True, null=True, verbose_name='謄本')),
                ('landArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='地坪(平方公尺)')),
                ('landHoldingPointPersonal', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='個人持分')),
                ('landHoldingPointAll', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='所有持分')),
                ('landRemarks', models.CharField(blank=True, max_length=100, null=True, verbose_name='備註')),
                ('landPresentValue', models.CharField(blank=True, max_length=100, null=True, verbose_name='土地現值')),
                ('landTotalArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='地坪總面積')),
                ('landAreaWidth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地寬度')),
                ('landAreaDepth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='土地深度')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lands', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='FinalDecision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalDecision', models.CharField(blank=True, max_length=10, null=True, verbose_name='最終判定')),
                ('subSigntrueA', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署人員1')),
                ('subSigntrueB', models.CharField(blank=True, max_length=10, null=True, verbose_name='副署人員2')),
                ('regionalHeadDate', models.CharField(blank=True, max_length=10, null=True, verbose_name='簽核日期')),
                ('subSigntrueDateA', models.CharField(blank=True, max_length=10, null=True, verbose_name='簽核日期')),
                ('subSigntrueDateB', models.CharField(blank=True, max_length=10, null=True, verbose_name='簽核日期')),
                ('regionalHead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finaldecisions', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='ClickList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicklistOccupy', models.BooleanField(default=False, verbose_name='01.占用鄰地？')),
                ('clicklistEegister', models.BooleanField(default=False, verbose_name='02.無未保存登記建物？')),
                ('clicklistParkingSpace', models.BooleanField(default=False, verbose_name='03.停車位(機車/汽車)？')),
                ('clicklistManagementFee', models.BooleanField(default=False, verbose_name='04.積欠管理費？')),
                ('clicklistRent', models.BooleanField(default=False, verbose_name='05.出租/出借/佔用？')),
                ('clicklistLeak', models.BooleanField(default=False, verbose_name='06.無嚴重漏水現象？')),
                ('clicklistEasyParking', models.BooleanField(default=False, verbose_name='07.停車方便？')),
                ('clicklistRailway', models.BooleanField(default=False, verbose_name='08.鄰近捷運站/台鐵站？')),
                ('clicklistVegetableMarket', models.BooleanField(default=False, verbose_name='09.鄰近菜市場？')),
                ('clicklistSupermarket', models.BooleanField(default=False, verbose_name='10.鄰近大賣場？')),
                ('clicklistSchool', models.BooleanField(default=False, verbose_name='11.鄰近學校？')),
                ('clicklistPark', models.BooleanField(default=False, verbose_name='12.鄰近公園？')),
                ('clicklistPostOffice', models.BooleanField(default=False, verbose_name='13.鄰近郵局/機關？')),
                ('clicklistMainRoad', models.BooleanField(default=False, verbose_name='14.鄰近幹道？')),
                ('clicklistWaterAndPowerFailure', models.BooleanField(default=False, verbose_name='15.斷水斷電？')),
                ('clicklistGoodVision', models.BooleanField(default=False, verbose_name='16.採光視野良好？')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clicklists', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='建號')),
                ('buildUrl', models.URLField(blank=True, null=True, verbose_name='謄本')),
                ('buildArea', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='建坪(平方公尺)')),
                ('buildHoldingPointPersonal', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='個人持分')),
                ('buildHoldingPointAll', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, verbose_name='所有持分')),
                ('buildTypeUse', models.CharField(blank=True, max_length=100, null=True, verbose_name='建物型')),
                ('buildUsePartition', models.CharField(blank=True, max_length=100, null=True, verbose_name='使用分區')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='yfcases.yfcase')),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctionDateFirst', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第一拍)')),
                ('auctionDateSecond', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第二拍)')),
                ('auctionDateThird', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第三拍)')),
                ('auctionDateFourth', models.CharField(blank=True, max_length=100, null=True, verbose_name='拍賣日(第四拍)')),
                ('auctionFloorPriceFirst', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第一拍)')),
                ('auctionFloorPriceSecond', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第二拍)')),
                ('auctionFloorPriceThird', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第三拍)')),
                ('auctionFloorPriceFourth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='底價(第四拍)')),
                ('auctionClickFirst', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第一拍)')),
                ('auctionClickSecond', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第二拍)')),
                ('auctionClickThird', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第三拍)')),
                ('auctionClickFourth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='點閱(第四拍)')),
                ('auctionMonitorFirst', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第一拍)')),
                ('auctionMonitorSecond', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第二拍)')),
                ('auctionMonitorThird', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第三拍)')),
                ('auctionMonitorFourth', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4, null=True, verbose_name='監控(第四拍)')),
                ('auctionMarginFirst', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第一拍)')),
                ('auctionMarginSecond', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第二拍)')),
                ('auctionMarginThird', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第三拍)')),
                ('auctionMarginFourth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='保証金(第四拍)')),
                ('yfcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auctions', to='yfcases.yfcase')),
            ],
        ),
    ]