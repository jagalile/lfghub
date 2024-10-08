# Generated by Django 5.0.6 on 2024-06-19 10:58

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("alias", models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="GameType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("alias", models.CharField(blank=True, max_length=200)),
                ("link", models.URLField(default="")),
            ],
        ),
        migrations.CreateModel(
            name="SocialMedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Looker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("avatar", models.ImageField(blank=True, upload_to="images/avatar")),
                (
                    "pronouns",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "He/Him/His"),
                            ("F", "She/Her/Hers"),
                            ("O", "They/Them/Theirs"),
                        ],
                        max_length=1,
                    ),
                ),
                ("bio", models.TextField(blank=True)),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AD", "Andorra"),
                            ("AE", "United Arab Emirates"),
                            ("AF", "Afghanistan"),
                            ("AG", "Antigua and Barbuda"),
                            ("AI", "Anguilla"),
                            ("AL", "Albania"),
                            ("AM", "Armenia"),
                            ("AO", "Angola"),
                            ("AQ", "Antarctica"),
                            ("AR", "Argentina"),
                            ("AS", "American Samoa"),
                            ("AT", "Austria"),
                            ("AU", "Australia"),
                            ("AW", "Aruba"),
                            ("AX", "Åland Islands"),
                            ("AZ", "Azerbaijan"),
                            ("BA", "Bosnia and Herzegovina"),
                            ("BB", "Barbados"),
                            ("BD", "Bangladesh"),
                            ("BE", "Belgium"),
                            ("BF", "Burkina Faso"),
                            ("BG", "Bulgaria"),
                            ("BH", "Bahrain"),
                            ("BI", "Burundi"),
                            ("BJ", "Benin"),
                            ("BL", "Saint Barthélemy"),
                            ("BM", "Bermuda"),
                            ("BN", "Brunei"),
                            ("BO", "Bolivia"),
                            ("BQ", "Caribbean Netherlands"),
                            ("BR", "Brazil"),
                            ("BS", "Bahamas"),
                            ("BT", "Bhutan"),
                            ("BV", "Bouvet Island"),
                            ("BW", "Botswana"),
                            ("BY", "Belarus"),
                            ("BZ", "Belize"),
                            ("CA", "Canada"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CD", "DR Congo"),
                            ("CF", "Central African Republic"),
                            ("CG", "Republic of the Congo"),
                            ("CH", "Switzerland"),
                            ("CI", "Côte d'Ivoire (Ivory Coast)"),
                            ("CK", "Cook Islands"),
                            ("CL", "Chile"),
                            ("CM", "Cameroon"),
                            ("CN", "China"),
                            ("CO", "Colombia"),
                            ("CR", "Costa Rica"),
                            ("CU", "Cuba"),
                            ("CV", "Cape Verde"),
                            ("CW", "Curaçao"),
                            ("CX", "Christmas Island"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czechia"),
                            ("DE", "Germany"),
                            ("DJ", "Djibouti"),
                            ("DK", "Denmark"),
                            ("DM", "Dominica"),
                            ("DO", "Dominican Republic"),
                            ("DZ", "Algeria"),
                            ("EC", "Ecuador"),
                            ("EE", "Estonia"),
                            ("EG", "Egypt"),
                            ("EH", "Western Sahara"),
                            ("ER", "Eritrea"),
                            ("ES", "Spain"),
                            ("ET", "Ethiopia"),
                            ("EU", "European Union"),
                            ("FI", "Finland"),
                            ("FJ", "Fiji"),
                            ("FK", "Falkland Islands"),
                            ("FM", "Micronesia"),
                            ("FO", "Faroe Islands"),
                            ("FR", "France"),
                            ("GA", "Gabon"),
                            ("GB", "United Kingdom"),
                            ("GB_ENG", "England"),
                            ("GB_NIR", "Northern Ireland"),
                            ("GB_SCT", "Scotland"),
                            ("GB_WLS", "Wales"),
                            ("GD", "Grenada"),
                            ("GE", "Georgia"),
                            ("GF", "French Guiana"),
                            ("GG", "Guernsey"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GL", "Greenland"),
                            ("GM", "Gambia"),
                            ("GN", "Guinea"),
                            ("GP", "Guadeloupe"),
                            ("GQ", "Equatorial Guinea"),
                            ("GR", "Greece"),
                            ("GS", "South Georgia"),
                            ("GT", "Guatemala"),
                            ("GU", "Guam"),
                            ("GW", "Guinea-Bissau"),
                            ("GY", "Guyana"),
                            ("HK", "Hong Kong"),
                            ("HM", "Heard Island and McDonald Islands"),
                            ("HN", "Honduras"),
                            ("HR", "Croatia"),
                            ("HT", "Haiti"),
                            ("HU", "Hungary"),
                            ("ID", "Indonesia"),
                            ("IE", "Ireland"),
                            ("IL", "Israel"),
                            ("IM", "Isle of Man"),
                            ("IN", "India"),
                            ("IO", "British Indian Ocean Territory"),
                            ("IQ", "Iraq"),
                            ("IR", "Iran"),
                            ("IS", "Iceland"),
                            ("IT", "Italy"),
                            ("JE", "Jersey"),
                            ("JM", "Jamaica"),
                            ("JO", "Jordan"),
                            ("JP", "Japan"),
                            ("KE", "Kenya"),
                            ("KG", "Kyrgyzstan"),
                            ("KH", "Cambodia"),
                            ("KI", "Kiribati"),
                            ("KM", "Comoros"),
                            ("KN", "Saint Kitts and Nevis"),
                            ("KP", "North Korea"),
                            ("KR", "South Korea"),
                            ("KW", "Kuwait"),
                            ("KY", "Cayman Islands"),
                            ("KZ", "Kazakhstan"),
                            ("LA", "Laos"),
                            ("LB", "Lebanon"),
                            ("LC", "Saint Lucia"),
                            ("LI", "Liechtenstein"),
                            ("LK", "Sri Lanka"),
                            ("LR", "Liberia"),
                            ("LS", "Lesotho"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("LV", "Latvia"),
                            ("LY", "Libya"),
                            ("MA", "Morocco"),
                            ("MC", "Monaco"),
                            ("MD", "Moldova"),
                            ("ME", "Montenegro"),
                            ("MF", "Saint Martin"),
                            ("MG", "Madagascar"),
                            ("MH", "Marshall Islands"),
                            ("MK", "North Macedonia"),
                            ("ML", "Mali"),
                            ("MM", "Myanmar"),
                            ("MN", "Mongolia"),
                            ("MO", "Macau"),
                            ("MP", "Northern Mariana Islands"),
                            ("MQ", "Martinique"),
                            ("MR", "Mauritania"),
                            ("MS", "Montserrat"),
                            ("MT", "Malta"),
                            ("MU", "Mauritius"),
                            ("MV", "Maldives"),
                            ("MW", "Malawi"),
                            ("MX", "Mexico"),
                            ("MY", "Malaysia"),
                            ("MZ", "Mozambique"),
                            ("NA", "Namibia"),
                            ("NC", "New Caledonia"),
                            ("NE", "Niger"),
                            ("NF", "Norfolk Island"),
                            ("NG", "Nigeria"),
                            ("NI", "Nicaragua"),
                            ("NL", "Netherlands"),
                            ("NO", "Norway"),
                            ("NP", "Nepal"),
                            ("NR", "Nauru"),
                            ("NU", "Niue"),
                            ("NZ", "New Zealand"),
                            ("OM", "Oman"),
                            ("PA", "Panama"),
                            ("PE", "Peru"),
                            ("PF", "French Polynesia"),
                            ("PG", "Papua New Guinea"),
                            ("PH", "Philippines"),
                            ("PK", "Pakistan"),
                            ("PL", "Poland"),
                            ("PM", "Saint Pierre and Miquelon"),
                            ("PN", "Pitcairn Islands"),
                            ("PR", "Puerto Rico"),
                            ("PS", "Palestine"),
                            ("PT", "Portugal"),
                            ("PW", "Palau"),
                            ("PY", "Paraguay"),
                            ("QA", "Qatar"),
                            ("RE", "Réunion"),
                            ("RO", "Romania"),
                            ("RS", "Serbia"),
                            ("RU", "Russia"),
                            ("RW", "Rwanda"),
                            ("SA", "Saudi Arabia"),
                            ("SB", "Solomon Islands"),
                            ("SC", "Seychelles"),
                            ("SD", "Sudan"),
                            ("SE", "Sweden"),
                            ("SG", "Singapore"),
                            ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                            ("SI", "Slovenia"),
                            ("SJ", "Svalbard and Jan Mayen"),
                            ("SK", "Slovakia"),
                            ("SL", "Sierra Leone"),
                            ("SM", "San Marino"),
                            ("SN", "Senegal"),
                            ("SO", "Somalia"),
                            ("SR", "Suriname"),
                            ("SS", "South Sudan"),
                            ("ST", "São Tomé and Príncipe"),
                            ("SV", "El Salvador"),
                            ("SX", "Sint Maarten"),
                            ("SY", "Syria"),
                            ("SZ", "Eswatini (Swaziland)"),
                            ("TC", "Turks and Caicos Islands"),
                            ("TD", "Chad"),
                            ("TF", "French Southern and Antarctic Lands"),
                            ("TG", "Togo"),
                            ("TH", "Thailand"),
                            ("TJ", "Tajikistan"),
                            ("TK", "Tokelau"),
                            ("TL", "Timor-Leste"),
                            ("TM", "Turkmenistan"),
                            ("TN", "Tunisia"),
                            ("TO", "Tonga"),
                            ("TR", "Turkey"),
                            ("TT", "Trinidad and Tobago"),
                            ("TV", "Tuvalu"),
                            ("TW", "Taiwan"),
                            ("TZ", "Tanzania"),
                            ("UA", "Ukraine"),
                            ("UG", "Uganda"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("UN", "United Nations"),
                            ("US", "United States"),
                            ("US_AK", "Alaska"),
                            ("US_AL", "Alabama"),
                            ("US_AR", "Arkansas"),
                            ("US_AZ", "Arizona"),
                            ("US_CA", "California"),
                            ("US_CO", "Colorado"),
                            ("US_CT", "Connecticut"),
                            ("US_DE", "Delaware"),
                            ("US_FL", "Florida"),
                            ("US_HI", "Hawaii"),
                            ("US_IA", "Iowa"),
                            ("US_ID", "Idaho"),
                            ("US_IL", "Illinois"),
                            ("US_IN", "Indiana"),
                            ("US_KS", "Kansas"),
                            ("US_KY", "Kentucky"),
                            ("US_LA", "Louisiana"),
                            ("US_MA", "Massachusetts"),
                            ("US_MD", "Maryland"),
                            ("US_ME", "Maine"),
                            ("US_MI", "Michigan"),
                            ("US_MN", "Minnesota"),
                            ("US_MO", "Missouri"),
                            ("US_MS", "Mississippi"),
                            ("US_MT", "Montana"),
                            ("US_NC", "North Carolina"),
                            ("US_ND", "North Dakota"),
                            ("US_NE", "Nebraska"),
                            ("US_NH", "New Hampshire"),
                            ("US_NJ", "New Jersey"),
                            ("US_NM", "New Mexico"),
                            ("US_NV", "Nevada"),
                            ("US_NY", "New York"),
                            ("US_OH", "Ohio"),
                            ("US_OK", "Oklahoma"),
                            ("US_OR", "Oregon"),
                            ("US_PA", "Pennsylvania"),
                            ("US_RI", "Rhode Island"),
                            ("US_SC", "South Carolina"),
                            ("US_SD", "South Dakota"),
                            ("US_TN", "Tennessee"),
                            ("US_TX", "Texas"),
                            ("US_UT", "Utah"),
                            ("US_VA", "Virginia"),
                            ("US_VT", "Vermont"),
                            ("US_WA", "Washington"),
                            ("US_WI", "Wisconsin"),
                            ("US_WV", "West Virginia"),
                            ("US_WY", "Wyoming"),
                            ("UY", "Uruguay"),
                            ("UZ", "Uzbekistan"),
                            ("VA", "Vatican City (Holy See)"),
                            ("VC", "Saint Vincent and the Grenadines"),
                            ("VE", "Venezuela"),
                            ("VG", "British Virgin Islands"),
                            ("VI", "United States Virgin Islands"),
                            ("VN", "Vietnam"),
                            ("VU", "Vanuatu"),
                            ("WF", "Wallis and Futuna"),
                            ("WS", "Samoa"),
                            ("XK", "Kosovo"),
                            ("YE", "Yemen"),
                            ("YT", "Mayotte"),
                            ("ZA", "South Africa"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "languages",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AA", "Afar"),
                            ("AB", "Abkhazian"),
                            ("AE", "Avestan"),
                            ("AF", "Afrikaans"),
                            ("AK", "Akan"),
                            ("AM", "Amharic"),
                            ("AN", "Aragonese"),
                            ("AR", "Arabic"),
                            ("AS", "Assamese"),
                            ("AV", "Avaric"),
                            ("AY", "Aymara"),
                            ("AZ", "Azerbaijani"),
                            ("BA", "Bashkir"),
                            ("BE", "Belarusian"),
                            ("BG", "Bulgarian"),
                            ("BH", "Bihari languages"),
                            ("BI", "Bislama"),
                            ("BM", "Bambara"),
                            ("BN", "Bengali"),
                            ("BO", "Tibetan"),
                            ("BR", "Breton"),
                            ("BS", "Bosnian"),
                            ("CA", "Catalan; Valencian"),
                            ("CE", "Chechen"),
                            ("CH", "Chamorro"),
                            ("CO", "Corsican"),
                            ("CR", "Cree"),
                            ("CS", "Czech"),
                            (
                                "CU",
                                "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
                            ),
                            ("CV", "Chuvash"),
                            ("CY", "Welsh"),
                            ("DA", "Danish"),
                            ("DE", "German"),
                            ("DV", "Divehi; Dhivehi; Maldivian"),
                            ("DZ", "Dzongkha"),
                            ("EE", "Ewe"),
                            ("EL", "Greek, Modern (1453-)"),
                            ("EN", "English"),
                            ("EO", "Esperanto"),
                            ("ES", "Spanish; Castilian"),
                            ("ET", "Estonian"),
                            ("EU", "Basque"),
                            ("FA", "Persian"),
                            ("FF", "Fulah"),
                            ("FI", "Finnish"),
                            ("FJ", "Fijian"),
                            ("FO", "Faroese"),
                            ("FR", "French"),
                            ("FY", "Western Frisian"),
                            ("GA", "Irish"),
                            ("GD", "Gaelic; Scottish Gaelic"),
                            ("GL", "Galician"),
                            ("GN", "Guarani"),
                            ("GU", "Gujarati"),
                            ("GV", "Manx"),
                            ("HA", "Hausa"),
                            ("HE", "Hebrew"),
                            ("HI", "Hindi"),
                            ("HO", "Hiri Motu"),
                            ("HR", "Croatian"),
                            ("HT", "Haitian; Haitian Creole"),
                            ("HU", "Hungarian"),
                            ("HY", "Armenian"),
                            ("HZ", "Herero"),
                            (
                                "IA",
                                "Interlingua (International Auxiliary Language Association)",
                            ),
                            ("ID", "Indonesian"),
                            ("IE", "Interlingue; Occidental"),
                            ("IG", "Igbo"),
                            ("II", "Sichuan Yi; Nuosu"),
                            ("IK", "Inupiaq"),
                            ("IO", "Ido"),
                            ("IS", "Icelandic"),
                            ("IT", "Italian"),
                            ("IU", "Inuktitut"),
                            ("JA", "Japanese"),
                            ("JV", "Javanese"),
                            ("KA", "Georgian"),
                            ("KG", "Kongo"),
                            ("KI", "Kikuyu; Gikuyu"),
                            ("KJ", "Kuanyama; Kwanyama"),
                            ("KK", "Kazakh"),
                            ("KL", "Kalaallisut; Greenlandic"),
                            ("KM", "Central Khmer"),
                            ("KN", "Kannada"),
                            ("KO", "Korean"),
                            ("KR", "Kanuri"),
                            ("KS", "Kashmiri"),
                            ("KU", "Kurdish"),
                            ("KV", "Komi"),
                            ("KW", "Cornish"),
                            ("KY", "Kirghiz; Kyrgyz"),
                            ("LA", "Latin"),
                            ("LB", "Luxembourgish; Letzeburgesch"),
                            ("LG", "Ganda"),
                            ("LI", "Limburgan; Limburger; Limburgish"),
                            ("LN", "Lingala"),
                            ("LO", "Lao"),
                            ("LT", "Lithuanian"),
                            ("LU", "Luba-Katanga"),
                            ("LV", "Latvian"),
                            ("MG", "Malagasy"),
                            ("MH", "Marshallese"),
                            ("MI", "Maori"),
                            ("MK", "Macedonian"),
                            ("ML", "Malayalam"),
                            ("MN", "Mongolian"),
                            ("MR", "Marathi"),
                            ("MS", "Malay"),
                            ("MT", "Maltese"),
                            ("MY", "Burmese"),
                            ("NA", "Nauru"),
                            ("NB", "Bokmål, Norwegian; Norwegian Bokmål"),
                            ("ND", "Ndebele, North; North Ndebele"),
                            ("NE", "Nepali"),
                            ("NG", "Ndonga"),
                            ("NL", "Dutch; Flemish"),
                            ("NN", "Norwegian Nynorsk; Nynorsk, Norwegian"),
                            ("NO", "Norwegian"),
                            ("NR", "Ndebele, South; South Ndebele"),
                            ("NV", "Navajo; Navaho"),
                            ("NY", "Chichewa; Chewa; Nyanja"),
                            ("OC", "Occitan (post 1500)"),
                            ("OJ", "Ojibwa"),
                            ("OM", "Oromo"),
                            ("OR", "Oriya"),
                            ("OS", "Ossetian; Ossetic"),
                            ("PA", "Panjabi; Punjabi"),
                            ("PI", "Pali"),
                            ("PL", "Polish"),
                            ("PS", "Pushto; Pashto"),
                            ("PT", "Portuguese"),
                            ("QU", "Quechua"),
                            ("RM", "Romansh"),
                            ("RN", "Rundi"),
                            ("RO", "Romanian; Moldavian; Moldovan"),
                            ("RU", "Russian"),
                            ("RW", "Kinyarwanda"),
                            ("SA", "Sanskrit"),
                            ("SC", "Sardinian"),
                            ("SD", "Sindhi"),
                            ("SE", "Northern Sami"),
                            ("SG", "Sango"),
                            ("SI", "Sinhala; Sinhalese"),
                            ("SK", "Slovak"),
                            ("SL", "Slovenian"),
                            ("SM", "Samoan"),
                            ("SN", "Shona"),
                            ("SO", "Somali"),
                            ("SQ", "Albanian"),
                            ("SR", "Serbian"),
                            ("SS", "Swati"),
                            ("ST", "Sotho, Southern"),
                            ("SU", "Sundanese"),
                            ("SV", "Swedish"),
                            ("SW", "Swahili"),
                            ("TA", "Tamil"),
                            ("TE", "Telugu"),
                            ("TG", "Tajik"),
                            ("TH", "Thai"),
                            ("TI", "Tigrinya"),
                            ("TK", "Turkmen"),
                            ("TL", "Tagalog"),
                            ("TN", "Tswana"),
                            ("TO", "Tonga (Tonga Islands)"),
                            ("TR", "Turkish"),
                            ("TS", "Tsonga"),
                            ("TT", "Tatar"),
                            ("TW", "Twi"),
                            ("TY", "Tahitian"),
                            ("UG", "Uighur; Uyghur"),
                            ("UK", "Ukrainian"),
                            ("UR", "Urdu"),
                            ("UZ", "Uzbek"),
                            ("VE", "Venda"),
                            ("VI", "Vietnamese"),
                            ("VO", "Volapük"),
                            ("WA", "Walloon"),
                            ("WO", "Wolof"),
                            ("XH", "Xhosa"),
                            ("YI", "Yiddish"),
                            ("YO", "Yoruba"),
                            ("ZA", "Zhuang; Chuang"),
                            ("ZH", "Chinese"),
                            ("ZU", "Zulu"),
                        ],
                        max_length=80,
                        null=True,
                    ),
                ),
                ("is_gm", models.BooleanField(default=False)),
                ("lfg_gm", models.BooleanField(default=False)),
                ("is_player", models.BooleanField(default=False)),
                ("lfg_player", models.BooleanField(default=False)),
                ("dark_theme", models.BooleanField(default=False)),
                (
                    "fav_gm_game",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fav_gm_game",
                        to="users.game",
                    ),
                ),
                (
                    "fav_player_game",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fav_player_game",
                        to="users.game",
                    ),
                ),
                (
                    "gm_games",
                    models.ManyToManyField(
                        blank=True, null=True, related_name="gm_games", to="users.game"
                    ),
                ),
                (
                    "player_games",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="player_games",
                        to="users.game",
                    ),
                ),
                (
                    "fav_game_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fav_game_type",
                        to="users.gametype",
                    ),
                ),
                (
                    "game_types",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="play_types",
                        to="users.gametype",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="LookerSocial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField()),
                (
                    "social_looker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "social_media",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.socialmedia",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="looker",
            name="socials",
            field=models.ManyToManyField(
                blank=True, null=True, to="users.lookersocial"
            ),
        ),
        migrations.AddField(
            model_name="looker",
            name="fav_platform",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fav_platform",
                to="users.platform",
            ),
        ),
        migrations.AddField(
            model_name="looker",
            name="platforms",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="platforms", to="users.platform"
            ),
        ),
    ]
