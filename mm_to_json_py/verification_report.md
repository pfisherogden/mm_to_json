# MDB Verification Report
Date: 2026-01-30 22:12:23.843013

## Round-Trip Results
| File | Status | Notes |
|---|---|---|
| 2025-07-19 CHAMPS/after meet - TVSL Championship Meet July 19, 2025.mdb | PASS |  |
| 2025-07-19 CHAMPS/before meet - 2025-07-19 CHAMPS-Meet2-MeetMgr.mdb | PASS |  |
| 2025-07-12 FAST @ DP/2025-07-12 FAST @ DP-Meet2-MeetMgr.mdb | PASS |  |
| 2025-06-21 Pleasanton Meadows @ DP/2025-06-21 Pleasanton Meadows @ DP-Meet2-MeetMgr.mdb | PASS |  |
| 2025-06-07 DP @ FAST/After Scratches - DP @ FAST 6.7.25.mdb | PASS |  |
| 2025-06-07 DP @ FAST/Pre-Meet 2025-06-07 DP @ FAST-Meet2-MeetMgr.mdb | PASS |  |
| 2025-06-07 DP @ FAST/After Meet DP @ FAST 6.7.25.mdb | PASS |  |
| 2025-07-02 Extra Chance/2025-07-02 Extra Chance-Meet2-MeetMgr.mdb | PASS |  |
| 2025-05-31 DP @ Bay Club/2025-05-31 DP @ Bay Club-Meet2-MeetMgr.mdb | PASS |  |
| 2025-05-31 DP @ Bay Club/Final - BCvsDP5-31-25@bc.mdb | PASS |  |
| 2025-06-28 Red vs. Black/TEST - 2025-06-28 Red vs-Meet2-MeetMgr.mdb | PASS |  |
| 2025-06-28 Red vs. Black/2025-06-28 Red vs-Meet2-MeetMgr.mdb | PASS |  |
| 2025-06-14 Briarhill @ DP/2025-06-14 Briarhill @ DP-Meet2-MeetMgr.mdb | PASS |  |

## Schema Analysis
Tables found across all MDBs:
### Table: `Agegroup`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| High_age | INT |
| Low_age | INT |

### Table: `AltScoring`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ind_score | FLOAT |
| rel_score | FLOAT |
| score_divno | INT |
| score_place | INT |
| score_sex | TEXT |

### Table: `Athlete`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Ath_Sex | TEXT |
| Ath_Sex_BS | TEXT |
| Ath_age | INT |
| Ath_no | LONG |
| Ath_stat | TEXT |
| Birth_date | SHORT_DATE_TIME |
| Citizen_of | TEXT |
| Comp_no | LONG |
| Disab_Exeptioncodes | TEXT |
| Disab_SBcode | INT |
| Disab_SDMSID | TEXT |
| Disab_SMcode | INT |
| Disab_Scode | INT |
| Div_no | LONG |
| First_name | TEXT |
| Home_addr1 | TEXT |
| Home_addr2 | TEXT |
| Home_celltele | TEXT |
| Home_city | TEXT |
| Home_cntry | TEXT |
| Home_daytele | TEXT |
| Home_email | TEXT |
| Home_emergcontact | TEXT |
| Home_emergtele | TEXT |
| Home_evetele | TEXT |
| Home_faxtele | TEXT |
| Home_prov | TEXT |
| Home_statenew | TEXT |
| Home_zip | TEXT |
| Initial | TEXT |
| Last_name | TEXT |
| Masters_RegVerified | BOOLEAN |
| PC_Hide | BOOLEAN |
| Picture_bmp | TEXT |
| Pref_name | TEXT |
| Reg_no | TEXT |
| Schl_yr | TEXT |
| Team_no | LONG |
| bcssa_type | TEXT |
| second_club | TEXT |

### Table: `CCrank`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Ath_no | LONG |
| Ath_sex | TEXT |
| Ath_stat | TEXT |
| Chute_no | INT |
| Chute_rank | LONG |
| Div_no | LONG |
| Ev_score | LONG |
| Event_ptr | LONG |
| Fin_Time | FLOAT |
| Fin_award | INT |
| Fin_course | TEXT |
| Fin_exh | TEXT |
| Fin_hand | BOOLEAN |
| Fin_jdplace | INT |
| Fin_place | INT |
| Fin_stat | TEXT |
| JDEv_score | LONG |
| Team_ltr | TEXT |
| Team_no | LONG |
| multi_age | INT |
| score_stat | TEXT |

### Table: `CCtime`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Ath_no | LONG |
| Chute_no | INT |
| Chute_rank | LONG |
| Event_ptr | LONG |
| Fin_Time | FLOAT |
| Fin_hand | BOOLEAN |
| Fin_stat | TEXT |

### Table: `CheckList`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| athlete_pref | BOOLEAN |
| dir_pref | BOOLEAN |
| divreg_names | BOOLEAN |
| entry_pref | BOOLEAN |
| entryfee_surcharges | BOOLEAN |
| event_setup | BOOLEAN |
| meet_setup | BOOLEAN |
| printer_setup | BOOLEAN |
| records_setup | BOOLEAN |
| report_pref | BOOLEAN |
| scbd_setup | BOOLEAN |
| scoring_setup | BOOLEAN |
| seeding_pref | BOOLEAN |
| session_setup | BOOLEAN |
| timestd_setup | BOOLEAN |
| timing_setup | BOOLEAN |

### Table: `CombinedEvent`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| CombEvent_ptr | LONG |
| Comm_1 | TEXT |
| Comm_2 | TEXT |
| Comm_3 | TEXT |
| Comm_4 | TEXT |
| Div_no | INT |
| Entry_fee | MONEY |
| Event_gender | TEXT |
| Event_ltr | TEXT |
| Event_no | INT |
| Event_note | TEXT |
| Event_ptr1 | LONG |
| Event_ptr10 | LONG |
| Event_ptr2 | LONG |
| Event_ptr3 | LONG |
| Event_ptr4 | LONG |
| Event_ptr5 | LONG |
| Event_ptr6 | LONG |
| Event_ptr7 | LONG |
| Event_ptr8 | LONG |
| Event_ptr9 | LONG |
| Event_sex | TEXT |
| High_Age | INT |
| Low_age | INT |
| Num_events | INT |
| Score_event | BOOLEAN |

### Table: `Divisions`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Div_name | TEXT |
| Div_no | LONG |
| div_abbr | TEXT |
| old_date | SHORT_DATE_TIME |
| young_date | SHORT_DATE_TIME |

### Table: `Dualteams`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ateam_no | LONG |
| bteam_no | LONG |
| team_gender | TEXT |

### Table: `Entry`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ActSeed_course | TEXT |
| ActualSeed_time | FLOAT |
| Alt_stat | BOOLEAN |
| Ath_no | LONG |
| Bonus_event | BOOLEAN |
| ConvSeed_course | TEXT |
| ConvSeed_time | FLOAT |
| Dec_stat | TEXT |
| Div_no | LONG |
| Ev_score | FLOAT |
| Event_ptr | LONG |
| Fin_Time | FLOAT |
| Fin_back1 | FLOAT |
| Fin_back2 | FLOAT |
| Fin_back3 | FLOAT |
| Fin_course | TEXT |
| Fin_dolphin1 | FLOAT |
| Fin_dolphin2 | FLOAT |
| Fin_dolphin3 | FLOAT |
| Fin_dqcode | TEXT |
| Fin_dqcodeSecond | TEXT |
| Fin_exh | TEXT |
| Fin_group | INT |
| Fin_heat | INT |
| Fin_heatplace | INT |
| Fin_jdheatplace | INT |
| Fin_jdplace | INT |
| Fin_lane | INT |
| Fin_pad | FLOAT |
| Fin_place | INT |
| Fin_points | INT |
| Fin_ptsplace | INT |
| Fin_reactiontime1 | TEXT |
| Fin_stat | TEXT |
| Fin_watch1 | FLOAT |
| JDEv_score | FLOAT |
| P_early_seed | BOOLEAN |
| Pre_Time | FLOAT |
| Pre_TimeType | TEXT |
| Pre_back1 | FLOAT |
| Pre_back2 | FLOAT |
| Pre_back3 | FLOAT |
| Pre_course | TEXT |
| Pre_dolphin1 | FLOAT |
| Pre_dolphin2 | FLOAT |
| Pre_dolphin3 | FLOAT |
| Pre_dqcode | TEXT |
| Pre_dqcodeSecond | TEXT |
| Pre_exh | TEXT |
| Pre_heat | INT |
| Pre_heatplace | INT |
| Pre_jdplace | INT |
| Pre_lane | INT |
| Pre_pad | FLOAT |
| Pre_place | INT |
| Pre_points | INT |
| Pre_reactiontime1 | TEXT |
| Pre_stat | TEXT |
| Pre_watch1 | FLOAT |
| Scr_stat | BOOLEAN |
| Seed_place | INT |
| Sem_Time | FLOAT |
| Sem_TimeType | TEXT |
| Sem_back1 | FLOAT |
| Sem_back2 | FLOAT |
| Sem_back3 | FLOAT |
| Sem_course | TEXT |
| Sem_dolphin1 | FLOAT |
| Sem_dolphin2 | FLOAT |
| Sem_dolphin3 | FLOAT |
| Sem_dqcode | TEXT |
| Sem_dqcodeSecond | TEXT |
| Sem_exh | TEXT |
| Sem_heat | INT |
| Sem_heatplace | INT |
| Sem_jdplace | INT |
| Sem_lane | INT |
| Sem_pad | FLOAT |
| Sem_place | INT |
| Sem_points | INT |
| Sem_reactiontime1 | TEXT |
| Sem_stat | TEXT |
| Sem_watch1 | FLOAT |
| Spec_stat | TEXT |
| dq_type | TEXT |
| early_seed | BOOLEAN |
| entry_method | TEXT |
| event_age | INT |
| fin_TimeType | TEXT |
| fin_adjuststat | TEXT |
| fin_divingdd | TEXT |
| fin_dqofficial | LONG |
| fin_heatltr | TEXT |
| pre_adjuststat | TEXT |
| pre_contacted | BOOLEAN |
| pre_divingdd | TEXT |
| pre_dqofficial | LONG |
| sem_adjuststat | TEXT |
| sem_divingdd | TEXT |
| sem_dqofficial | LONG |
| super_finfinalist | BOOLEAN |
| super_prefinalist | BOOLEAN |

### Table: `Event`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ABC_Style | BOOLEAN |
| ABCfinal_order | TEXT |
| Auto_seed | BOOLEAN |
| Checkin_enddate | SHORT_DATE_TIME |
| Checkin_endtime | LONG |
| Checkin_startdate | SHORT_DATE_TIME |
| Checkin_starttime | LONG |
| Comm_1 | TEXT |
| Comm_2 | TEXT |
| Comm_3 | TEXT |
| Comm_4 | TEXT |
| Custom_ABCFinal | BOOLEAN |
| Div_no | INT |
| Entry_fee | MONEY |
| Event_Type | TEXT |
| Event_dist | FLOAT |
| Event_gender | TEXT |
| Event_ltr | TEXT |
| Event_no | INT |
| Event_note | TEXT |
| Event_ptr | LONG |
| Event_rounds | INT |
| Event_sex | TEXT |
| Event_stat | TEXT |
| Event_stroke | TEXT |
| EvtMaxAgeFor_CFinal | INT |
| EvtMaxAgeNumHeats_CFinal | INT |
| FastTimeStd_Abbr | TEXT |
| Fin_AwardsPrinted | BOOLEAN |
| Finals_LanesVary | BOOLEAN |
| Finals_LanesVaryOrder | TEXT |
| Finheat_order | TEXT |
| Heats_infinal | TEXT |
| Heats_insemi | INT |
| High_Age | INT |
| Ind_rel | TEXT |
| Is_locked | BOOLEAN |
| Locked_by | TEXT |
| Locked_list | TEXT |
| Low_age | INT |
| Multi_age | BOOLEAN |
| Multi_ageScnd | BOOLEAN |
| Multiage_BestRestFinal | BOOLEAN |
| Multiage_SuperFinal | BOOLEAN |
| Multiage_SuperSeed | BOOLEAN |
| Num_BestHeatsTimedFinal | INT |
| Num_HeatsInFinal | INT |
| Num_HeatsInTimedFinalToScore | INT |
| Num_LanesInBestHeatsTimedFinal | INT |
| Num_RelayLegs | INT |
| Num_dives | INT |
| Num_finlanes | INT |
| Num_prelanes | INT |
| Num_semlanes | INT |
| Pads_BothEnds | BOOLEAN |
| Pads_BothEndsFinals | BOOLEAN |
| Pre_AwardsPrinted | BOOLEAN |
| Preheat_order | TEXT |
| PrelimsAs_ExtendedFinal | BOOLEAN |
| Relay_size | INT |
| ScoreTimedFinal_asABC | BOOLEAN |
| Score_event | BOOLEAN |
| SeedMultiAge_OldToYoung | BOOLEAN |
| Sem_AwardsPrinted | BOOLEAN |
| SlowTimeStd_Abbr | TEXT |
| Std_lanes | TEXT |
| SuperFinal_ElimOldAgeGrp | BOOLEAN |
| Suppress_distance | BOOLEAN |
| Suppress_stroke | BOOLEAN |
| Swimoff_Created | SHORT_DATE_TIME |
| Swimoff_SourcePtr | LONG |
| Swimoff_SourceRndLtr | TEXT |
| TimedFinal_LanesVary | BOOLEAN |
| Twoperlane_req | BOOLEAN |
| fin_actualstarttime | LONG |
| pre_actualstarttime | LONG |
| sem_actualstarttime | LONG |

### Table: `EventGetTimes`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Event_ptr | LONG |
| Get_Date | SHORT_DATE_TIME |
| Get_Time | LONG |
| Heat_no | INT |
| Now_Date | SHORT_DATE_TIME |
| Now_Time | LONG |
| Race_number | TEXT |
| Rnd_ltr | TEXT |
| Vendor_abbr | TEXT |

### Table: `MEETMOBILE2OPTIONS`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Addr | TEXT |
| AgencyID | TEXT |
| AnnounceEV5_uploaded | BOOLEAN |
| City | TEXT |
| Classification | TEXT |
| Cntry | TEXT |
| Contract_PersonBirth | SHORT_DATE_TIME |
| Contract_PersonBirthMeetSharing | SHORT_DATE_TIME |
| Contract_PersonName | TEXT |
| Contract_PersonNameMeetSharing | TEXT |
| Contract_agreed | BOOLEAN |
| Contract_agreedMeetSharing | BOOLEAN |
| DoNotShow_MeetSharingImportMsg | BOOLEAN |
| DoNotShow_timeline | BOOLEAN |
| EMail | TEXT |
| EV5_uploaded | BOOLEAN |
| FileSharingEntryLimitsOk | BOOLEAN |
| FileSharingEvtsOk | BOOLEAN |
| FileSharingMeetID | LONG |
| FileSharingMeetSetupOk | BOOLEAN |
| FileSharingPricingOk | BOOLEAN |
| FileSharingQualTimesOk | BOOLEAN |
| FirstName | TEXT |
| HeatPsych_choice | INT |
| HeatSheetsAre_Free | BOOLEAN |
| Heatpsych_uploaded | BOOLEAN |
| Heatsheet_amount | FLOAT |
| LastName | TEXT |
| License | TEXT |
| MeetMobile2MeetID | LONG |
| MeetResultsID | LONG |
| NoShowActiveComSetup | BOOLEAN |
| NotInterestedIn_FileSharing | BOOLEAN |
| NotInterestedIn_MeetMobile | BOOLEAN |
| OMEWebSite | TEXT |
| PayTo | TEXT |
| Phone | TEXT |
| ResultsFile_uploaded | BOOLEAN |
| SecAddr | TEXT |
| SharingEV5_uploaded | BOOLEAN |
| State | TEXT |
| TeamName | TEXT |
| Teamscoring_choice | INT |
| TimeZone | TEXT |
| Token | TEXT |
| WebSite | TEXT |
| Zip | TEXT |

### Table: `Masters`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Meet_type | INT |
| pool_city | TEXT |
| pool_lmsc | TEXT |
| pool_name | TEXT |
| pool_state | TEXT |
| record_name | TEXT |
| ref_name | TEXT |
| sendto_address | TEXT |
| sendto_city | TEXT |
| sendto_email | TEXT |
| sendto_name | TEXT |
| sendto_state | TEXT |
| sendto_zip | TEXT |
| sub_address | TEXT |
| sub_city | TEXT |
| sub_email | TEXT |
| sub_name | TEXT |
| sub_phone | TEXT |
| sub_state | TEXT |
| sub_zip | TEXT |
| timer_type | INT |

### Table: `Meet`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| APNews_Dir | TEXT |
| A_Relaysonly | BOOLEAN |
| AllowSameEvent_DupRelayNames | BOOLEAN |
| BCSSA_DivbyTimeStd | BOOLEAN |
| Backup_Dir | TEXT |
| Calc_date | SHORT_DATE_TIME |
| Competition_Code | TEXT |
| CountTimeTrial_Events | BOOLEAN |
| Custom_QualTimes | BOOLEAN |
| DQCodes_Type | TEXT |
| DisabledDoNot_AdvanceToFinals | BOOLEAN |
| DisabledIgnoreQualTime_ForScoring | BOOLEAN |
| DisabledSeedWithAgeGroup_IfTimedFinalSuperSeed | BOOLEAN |
| DisplayNTfor_TimesUnder5Sec | BOOLEAN |
| Display_ActualEntryTime | BOOLEAN |
| Enter_AthStat | BOOLEAN |
| Enter_ages | BOOLEAN |
| Enter_birthcentury | BOOLEAN |
| Enter_birthdate | BOOLEAN |
| Enter_schoolyr | BOOLEAN |
| EntryEligibility_date | SHORT_DATE_TIME |
| ExcludeNTEntries_WhenImporting | BOOLEAN |
| Export_Dir | TEXT |
| Facility_Surcharge | MONEY |
| FastestHeat_SomeLanesDoNotScore | BOOLEAN |
| Flag_FastestRecordOnly | BOOLEAN |
| FlatHtml_Dir | TEXT |
| Flighted_BasedOnResultsTime | BOOLEAN |
| Import_Dir | TEXT |
| IsCanadian_Masters | BOOLEAN |
| Last_updated | TEXT |
| Lastname_first | BOOLEAN |
| Lock_Reseed | BOOLEAN |
| Meet_USMastersMeetID | TEXT |
| Meet_addr1 | TEXT |
| Meet_addr2 | TEXT |
| Meet_altitude | LONG |
| Meet_city | TEXT |
| Meet_class | INT |
| Meet_country | TEXT |
| Meet_course | INT |
| Meet_end | SHORT_DATE_TIME |
| Meet_header1 | TEXT |
| Meet_header2 | TEXT |
| Meet_hostlsc | TEXT |
| Meet_idformat | INT |
| Meet_location | TEXT |
| Meet_lsc | TEXT |
| Meet_meettype | INT |
| Meet_name1 | TEXT |
| Meet_start | SHORT_DATE_TIME |
| Meet_state | TEXT |
| Meet_zip | TEXT |
| MixedRelays_DividedPoints | BOOLEAN |
| NonConforming_PoolFactor | FLOAT |
| PenaltyPts_ForNS | FLOAT |
| PenaltyTimeSec_ForCombEvtDQ | FLOAT |
| PointsAwarded_ForDQ | FLOAT |
| PointsAwarded_ForExh | BOOLEAN |
| PointsAwarded_ForNT | FLOAT |
| PointsAwarded_ForScratch | FLOAT |
| Pool1_name | TEXT |
| Pool2_name | TEXT |
| Punct_names | BOOLEAN |
| Punct_recholders | BOOLEAN |
| Punct_teams | BOOLEAN |
| QualNonConformCourse_UseMinStd | BOOLEAN |
| RankDisabled_ByPoints | BOOLEAN |
| Read_Only | BOOLEAN |
| RelayNames_LinkByLSC | BOOLEAN |
| RelayOnly_Surcharge | MONEY |
| RelaysAlternate_TwoFastestFirst | BOOLEAN |
| RelaysAs_4x100Style | BOOLEAN |
| RestoreFrom_Dir | TEXT |
| RestoreTo_Dir | TEXT |
| Scores_afterevt | BOOLEAN |
| ShowFirstName_OverPreferred | BOOLEAN |
| ShowYear_InPlaceOfAge | BOOLEAN |
| Show_AgeandBirthYear | BOOLEAN |
| Show_HyTekDecimals | BOOLEAN |
| Show_countrycode | BOOLEAN |
| Show_secondclub | BOOLEAN |
| SortTeamCombos_ByTeamName | BOOLEAN |
| SuppressTimes_NotMeetQualTime | BOOLEAN |
| Suppress_ResultsAdvQ | BOOLEAN |
| Suppress_SplitsForDQs | BOOLEAN |
| Suppress_SplitsForDQsRelay | BOOLEAN |
| Suppress_TimeStdAbbr | BOOLEAN |
| TimeAdj_Method | TEXT |
| UseNonConforming_PoolFactor | BOOLEAN |
| Use_AltTeamAbbr | BOOLEAN |
| Use_hometown | BOOLEAN |
| Using_twopools | BOOLEAN |
| abcfinal_order | TEXT |
| anyone_onrelay | BOOLEAN |
| apnews_team | TEXT |
| athlete_earlysurcharge | MONEY |
| athlete_earlysurchargedate | SHORT_DATE_TIME |
| athlete_latesurcharge | MONEY |
| athlete_latesurchargedate | SHORT_DATE_TIME |
| autobackup_interval | INT |
| autoinc_compno | BOOLEAN |
| check_times | BOOLEAN |
| copies_toprinter | INT |
| countrelay_alt | BOOLEAN |
| course_order | TEXT |
| diffpts_eachdivision | BOOLEAN |
| diffpts_malefemale | BOOLEAN |
| directly_toprinter | BOOLEAN |
| double_endedsplits | BOOLEAN |
| dual_evenodd | BOOLEAN |
| dualseeding_altunusedlane | BOOLEAN |
| dualteam_lane1 | LONG |
| dualteam_lane10 | LONG |
| dualteam_lane11 | LONG |
| dualteam_lane12 | LONG |
| dualteam_lane2 | LONG |
| dualteam_lane3 | LONG |
| dualteam_lane4 | LONG |
| dualteam_lane5 | LONG |
| dualteam_lane6 | LONG |
| dualteam_lane7 | LONG |
| dualteam_lane8 | LONG |
| dualteam_lane9 | LONG |
| enter_citizenof | BOOLEAN |
| enterkey_astab | BOOLEAN |
| entry_OMEopendate | SHORT_DATE_TIME |
| entry_OpenDate | SHORT_DATE_TIME |
| entry_deadline | SHORT_DATE_TIME |
| entry_msg | TEXT |
| entrylimits_warn | BOOLEAN |
| entrymax_total | INT |
| entryqual_faster | BOOLEAN |
| exh_infinal | BOOLEAN |
| firstinitial_fulllastname | BOOLEAN |
| flag_overachievers | BOOLEAN |
| flag_underachievers | BOOLEAN |
| flighted_flightcount | INT |
| flighted_inclDQ | BOOLEAN |
| flighted_minentries | INT |
| foreign_getteampoints | BOOLEAN |
| foreign_infinal | BOOLEAN |
| include_sanction | BOOLEAN |
| include_swimupsinteamscore | BOOLEAN |
| indmax_perath | INT |
| indmaxadvance_perteam | INT |
| indmaxscorers_perteam | INT |
| indtopmany_awards | INT |
| indtopmany_awardsSr | INT |
| language_choice | TEXT |
| lastname_asinitial | BOOLEAN |
| masters_agegrpsskip | INT |
| masters_bytimeonly | BOOLEAN |
| masters_indlowage | INT |
| masters_rellowage | INT |
| maxagefor_cfinal | INT |
| maxforeign_infinal | INT |
| meet_meetstyle | INT |
| meet_numlanes | INT |
| military_time | BOOLEAN |
| nonconform_last | BOOLEAN |
| open_lowage | INT |
| open_senior_none | TEXT |
| pentscoring_usedqtime | BOOLEAN |
| pointsbasedon_seedtime | BOOLEAN |
| pointsfor_overachievers | BOOLEAN |
| pointsfor_underachievers | BOOLEAN |
| prelimheats_circle | INT |
| prelimheats_circledist | INT |
| referee_homphone | TEXT |
| referee_name | TEXT |
| referee_offphone | TEXT |
| relmax_perath | INT |
| relmaxadvance_perteam | INT |
| relmaxscorers_perteam | INT |
| reltopmany_awards | INT |
| reltopmany_awardsSr | INT |
| report_headersonly | BOOLEAN |
| sanction_number | TEXT |
| scbd_cycle | BOOLEAN |
| scbd_cycleseconds | INT |
| scbd_names | INT |
| scbd_port | INT |
| scbd_punctuation | INT |
| scbd_relaynames | INT |
| scbd_vendor | TEXT |
| score_Arelayonly | BOOLEAN |
| score_fastestheatonly | BOOLEAN |
| scoreonly_ifexceedqualtime | BOOLEAN |
| seed_exhlast | BOOLEAN |
| show_initial | BOOLEAN |
| showathlete_status | BOOLEAN |
| special_parapoints | INT |
| special_points | INT |
| strict_evenodd | BOOLEAN |
| strict_evenoddfastestheatonly | BOOLEAN |
| suppress_Arelay | BOOLEAN |
| suppress_jd | BOOLEAN |
| suppress_lsc | BOOLEAN |
| suppress_smallx | BOOLEAN |
| swimmer_surcharge | MONEY |
| team_evenlanes | LONG |
| team_oddlanes | LONG |
| team_surcharge | MONEY |
| thirteenandover_assenior | BOOLEAN |
| timedfinal_circleseed | BOOLEAN |
| timedfinalnonconform_last | BOOLEAN |
| timer_port | INT |
| timer_vendor | TEXT |
| turnon_autobackup | BOOLEAN |
| ucase_names | BOOLEAN |
| ucase_recholders | BOOLEAN |
| ucase_teams | BOOLEAN |
| under_eventname | BOOLEAN |
| use_compnumbers | BOOLEAN |
| useeventsex_teamscore | BOOLEAN |
| win_mm | BOOLEAN |

### Table: `MemorizedReports`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| AddApost_ClassYear | BOOLEAN |
| Add_LineSpace | BOOLEAN |
| AddrSort_ByTeam | BOOLEAN |
| AddrSort_ByZip | BOOLEAN |
| AthUseAbbr_ForTeam | BOOLEAN |
| BAG_CATS | BOOLEAN |
| CombineDivisions_ForTeamPoints | BOOLEAN |
| Combined_BothMustScore | BOOLEAN |
| DQs_Only | BOOLEAN |
| Date_Time | INT |
| Dbl_Space | BOOLEAN |
| Div_Abbr | TEXT |
| DotMatrix_LabelChoice | TEXT |
| Evt_Gender | INT |
| Evt_HighAge | INT |
| Evt_IndivOrRelay | INT |
| Evt_LowAge | INT |
| Evt_Round | INT |
| Flat_HTML | BOOLEAN |
| High_Lane | INT |
| ID_Type | INT |
| Ignore_Psych | BOOLEAN |
| Incl_AltInEntryCount | BOOLEAN |
| Incl_AthNoEntries | BOOLEAN |
| Incl_AthNoEntries4Col | BOOLEAN |
| Incl_Backups | BOOLEAN |
| Incl_BirthDate | BOOLEAN |
| Incl_Coaches | BOOLEAN |
| Incl_CompNo | BOOLEAN |
| Incl_CompNo4Col | BOOLEAN |
| Incl_DQCodes | BOOLEAN |
| Incl_EmptyLanes | BOOLEAN |
| Incl_EntryTimes | BOOLEAN |
| Incl_EvtComments | BOOLEAN |
| Incl_FemaleTeamScore | BOOLEAN |
| Incl_HeatLane | BOOLEAN |
| Incl_LogosinFooter | BOOLEAN |
| Incl_MaleTeamScore | BOOLEAN |
| Incl_NoEntries | BOOLEAN |
| Incl_NoShows | BOOLEAN |
| Incl_PriorResults | BOOLEAN |
| Incl_PriorResultsSplits | BOOLEAN |
| Incl_QualTimes | BOOLEAN |
| Incl_QualifiedAlts | BOOLEAN |
| Incl_ReactionTimes | BOOLEAN |
| Incl_Records | BOOLEAN |
| Incl_RegID | BOOLEAN |
| Incl_Rnd1Alt | BOOLEAN |
| Incl_ScrInEntryCount | BOOLEAN |
| Incl_Scratches | BOOLEAN |
| Incl_SeeBreak | BOOLEAN |
| Incl_SpecPts | BOOLEAN |
| Incl_TeamAddr | BOOLEAN |
| Incl_TeamPts | BOOLEAN |
| Incl_TeamScore | BOOLEAN |
| Incl_TimeStds | BOOLEAN |
| Incl_TimeTrials | BOOLEAN |
| LaneTimer_Pads | BOOLEAN |
| Laser_LabelChoice | TEXT |
| Line_ForResults | BOOLEAN |
| Low_Lane | INT |
| Mem_Name | TEXT |
| Mem_Ptr | LONG |
| Mem_Type | INT |
| MultiAge_Split | BOOLEAN |
| NoShows_Only | BOOLEAN |
| NumAth_PerPage | INT |
| Num_Columns | INT |
| Num_RelayNames | INT |
| OneEvent_PerPage | BOOLEAN |
| OneHeat_PerPage | BOOLEAN |
| Page_Break | BOOLEAN |
| PtBreakOut_HighPt | BOOLEAN |
| QualClub_Scorers | BOOLEAN |
| Qual_Club | BOOLEAN |
| RTF_export | BOOLEAN |
| Ref_Format | BOOLEAN |
| Report_Format | INT |
| Report_Type | INT |
| Results_ByHeat | BOOLEAN |
| Results_ByHeatInclLane | BOOLEAN |
| Score_Combined | BOOLEAN |
| Score_CombinedBoth | BOOLEAN |
| Score_Female | BOOLEAN |
| Score_Male | BOOLEAN |
| ScrAltExhSpec_Filters | INT |
| Scratches_Only | BOOLEAN |
| Sep_ABFinal | BOOLEAN |
| Sess_Row | LONG |
| Show_CheckIn | BOOLEAN |
| Show_Ranks | BOOLEAN |
| Show_SeedTimes | BOOLEAN |
| Show_StartTimes | BOOLEAN |
| Sort_Order | INT |
| Sort_OrderAthAge | INT |
| Splits_Choice | INT |
| Team_Abbr | TEXT |
| Top_HowMany | INT |
| UseBestTimes_AllRounds | BOOLEAN |
| UseDQTimesfor_CombinedEvents | BOOLEAN |
| UseLaser_Label | INT |

### Table: `Multiage`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Heats_infinal | TEXT |
| Num_Heatsinfinal | INT |
| event_ptr | LONG |
| high_age | INT |
| low_age | INT |

### Table: `MultiageScnd`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| event_ptr | LONG |
| high_age | INT |
| low_age | INT |

### Table: `OMEOPTIONS`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ActiveMeetID | LONG |
| Addr | TEXT |
| AgencyID | TEXT |
| City | TEXT |
| Classification | TEXT |
| Cntry | TEXT |
| EMail | TEXT |
| EMailFrom | TEXT |
| EMailSubject | TEXT |
| EMailText | TEXT |
| EV4_uploaded | BOOLEAN |
| FirstName | TEXT |
| LastName | TEXT |
| License | TEXT |
| NoShowActiveComSetup | BOOLEAN |
| NoShowMeetList | BOOLEAN |
| NoShowMeetSetup | BOOLEAN |
| OMEEntryStyle | BYTE |
| OMEReviewTime | BYTE |
| OMEWebSite | TEXT |
| PayTo | TEXT |
| Phone | TEXT |
| SecAddr | TEXT |
| State | TEXT |
| TeamName | TEXT |
| TimeZone | TEXT |
| Token | TEXT |
| WebSite | TEXT |
| Zip | TEXT |

### Table: `Officials`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| First_name | TEXT |
| Home_email | TEXT |
| Initial | TEXT |
| Last_name | TEXT |
| Official_no | LONG |
| Pref_name | TEXT |

### Table: `RecordTags`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| allow_exh | BOOLEAN |
| allow_foreigner | BOOLEAN |
| tag_flag | TEXT |
| tag_lsc | TEXT |
| tag_name | TEXT |
| tag_order | INT |
| tag_ptr | LONG |
| team_no | LONG |

### Table: `Records`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Record_Holder | TEXT |
| Record_Holderteam | TEXT |
| Record_Time | FLOAT |
| Record_course | TEXT |
| Record_day | INT |
| Record_month | INT |
| Record_teamabbr | TEXT |
| Record_teamlsc | TEXT |
| Record_year | INT |
| Relay_Names | TEXT |
| div_abbr | TEXT |
| high_Age | INT |
| low_age | INT |
| tag_dist | LONG |
| tag_gender | TEXT |
| tag_indrel | TEXT |
| tag_ptr | LONG |
| tag_stroke | TEXT |

### Table: `RecordsApp`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| adminref_name | TEXT |
| app_bottomnote1 | TEXT |
| app_bottomnote2 | TEXT |
| app_bottomnote3 | TEXT |
| app_bottomnote4 | TEXT |
| app_date | TEXT |
| app_title | TEXT |
| app_topnote1 | TEXT |
| app_topnote2 | TEXT |
| app_topnote3 | TEXT |
| app_topnote4 | TEXT |
| record_name | TEXT |
| referree_name | TEXT |
| sendto_address1 | TEXT |
| sendto_address2 | TEXT |
| sendto_city | TEXT |
| sendto_email | TEXT |
| sendto_name | TEXT |
| sendto_state | TEXT |
| sendto_zip | TEXT |
| timer_type | INT |

### Table: `RecordsbyEvent`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Record_Holder | TEXT |
| Record_Holderteam | TEXT |
| Record_Time | FLOAT |
| Record_course | TEXT |
| Record_day | INT |
| Record_month | INT |
| Record_teamabbr | TEXT |
| Record_teamlsc | TEXT |
| Record_year | INT |
| Relay_Names | TEXT |
| div_abbr | TEXT |
| event_ptr | LONG |
| hide_me | BOOLEAN |
| high_Age | INT |
| low_age | INT |
| tag_gender | TEXT |
| tag_ptr | LONG |

### Table: `Regions`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Reg_abbr | TEXT |
| Reg_name | TEXT |
| Reg_no | LONG |
| combined_size | INT |
| fem_size | INT |
| male_size | INT |

### Table: `Relay`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ActSeed_course | TEXT |
| ActualSeed_time | FLOAT |
| Alt_stat | BOOLEAN |
| Bonus_event | BOOLEAN |
| ConvSeed_course | TEXT |
| ConvSeed_time | FLOAT |
| Dec_stat | TEXT |
| Div_no | LONG |
| Ev_score | FLOAT |
| Event_ptr | LONG |
| Fin_Time | FLOAT |
| Fin_TimeType | TEXT |
| Fin_back1 | FLOAT |
| Fin_back2 | FLOAT |
| Fin_back3 | FLOAT |
| Fin_course | TEXT |
| Fin_dolphin1 | FLOAT |
| Fin_dolphin2 | FLOAT |
| Fin_dolphin3 | FLOAT |
| Fin_dqcode | TEXT |
| Fin_dqcodeSecond | TEXT |
| Fin_exh | TEXT |
| Fin_group | INT |
| Fin_heat | INT |
| Fin_heatltr | TEXT |
| Fin_heatplace | INT |
| Fin_jdheatplace | INT |
| Fin_jdplace | INT |
| Fin_lane | INT |
| Fin_pad | FLOAT |
| Fin_place | INT |
| Fin_points | INT |
| Fin_ptsplace | INT |
| Fin_reactiontime1 | TEXT |
| Fin_reactiontime2 | TEXT |
| Fin_reactiontime3 | TEXT |
| Fin_reactiontime4 | TEXT |
| Fin_stat | TEXT |
| Fin_watch1 | FLOAT |
| JDEv_score | FLOAT |
| Pre_Time | FLOAT |
| Pre_TimeType | TEXT |
| Pre_back1 | FLOAT |
| Pre_back2 | FLOAT |
| Pre_back3 | FLOAT |
| Pre_course | TEXT |
| Pre_dolphin1 | FLOAT |
| Pre_dolphin2 | FLOAT |
| Pre_dolphin3 | FLOAT |
| Pre_dqcode | TEXT |
| Pre_dqcodeSecond | TEXT |
| Pre_exh | TEXT |
| Pre_heat | INT |
| Pre_heatplace | INT |
| Pre_jdplace | INT |
| Pre_lane | INT |
| Pre_pad | FLOAT |
| Pre_place | INT |
| Pre_points | INT |
| Pre_reactiontime1 | TEXT |
| Pre_reactiontime2 | TEXT |
| Pre_reactiontime3 | TEXT |
| Pre_reactiontime4 | TEXT |
| Pre_stat | TEXT |
| Pre_watch1 | FLOAT |
| Rel_age | INT |
| Rel_sex | TEXT |
| Relay_no | LONG |
| Scr_stat | BOOLEAN |
| Seed_place | INT |
| Sem_Time | FLOAT |
| Sem_TimeType | TEXT |
| Sem_back1 | FLOAT |
| Sem_back2 | FLOAT |
| Sem_back3 | FLOAT |
| Sem_course | TEXT |
| Sem_dolphin1 | FLOAT |
| Sem_dolphin2 | FLOAT |
| Sem_dolphin3 | FLOAT |
| Sem_dqcode | TEXT |
| Sem_dqcodeSecond | TEXT |
| Sem_exh | TEXT |
| Sem_heat | INT |
| Sem_heatplace | INT |
| Sem_jdplace | INT |
| Sem_lane | INT |
| Sem_pad | FLOAT |
| Sem_place | INT |
| Sem_points | INT |
| Sem_reactiontime1 | TEXT |
| Sem_reactiontime2 | TEXT |
| Sem_reactiontime3 | TEXT |
| Sem_reactiontime4 | TEXT |
| Sem_stat | TEXT |
| Sem_watch1 | FLOAT |
| Spec_stat | TEXT |
| Team_ltr | TEXT |
| Team_no | LONG |
| dq_type | TEXT |
| early_seed | BOOLEAN |
| entry_method | TEXT |
| fin_adjuststat | TEXT |
| fin_dqofficial | LONG |
| pre_adjuststat | TEXT |
| pre_contacted | BOOLEAN |
| pre_dqofficial | LONG |
| sem_adjuststat | TEXT |
| sem_dqofficial | LONG |

### Table: `RelayNames`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Ath_no | LONG |
| Event_ptr | LONG |
| Event_round | TEXT |
| Pos_no | INT |
| Relay_no | LONG |
| Team_ltr | TEXT |
| Team_no | LONG |

### Table: `ScoreLanes`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| lane_00 | BOOLEAN |
| lane_01 | BOOLEAN |
| lane_02 | BOOLEAN |
| lane_03 | BOOLEAN |
| lane_04 | BOOLEAN |
| lane_05 | BOOLEAN |
| lane_06 | BOOLEAN |
| lane_07 | BOOLEAN |
| lane_08 | BOOLEAN |
| lane_09 | BOOLEAN |
| lane_10 | BOOLEAN |
| lane_11 | BOOLEAN |
| lane_12 | BOOLEAN |

### Table: `Scoring`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| ind_score | FLOAT |
| rel_score | FLOAT |
| score_divno | INT |
| score_place | INT |
| score_sex | TEXT |

### Table: `ScoringImprovement`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| diff_hightime | FLOAT |
| diff_lowtime | FLOAT |
| list_no | INT |
| pt_score | FLOAT |
| swim_score | FLOAT |

### Table: `Session`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Sess_backinterval | INT |
| Sess_chaseinterval | INT |
| Sess_course | TEXT |
| Sess_day | INT |
| Sess_divinginterval | INT |
| Sess_entrymax | INT |
| Sess_entrymaxind | INT |
| Sess_entrymaxrel | INT |
| Sess_interval | INT |
| Sess_ltr | TEXT |
| Sess_name | TEXT |
| Sess_no | INT |
| Sess_ptr | LONG |
| Sess_starttime | LONG |

### Table: `Sessitem`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| AltHeats_StartCount | INT |
| Alt_With | BOOLEAN |
| Delay_desc | TEXT |
| Delay_seconds | LONG |
| EventTo_AlternateWith | LONG |
| Event_Interval | LONG |
| Event_ptr | LONG |
| Rept_type | TEXT |
| Sess_order | LONG |
| Sess_ptr | LONG |
| Sess_rnd | TEXT |
| Timed_finalheats | INT |

### Table: `Split`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Ath_no | LONG |
| Event_ptr | LONG |
| Relay_no | LONG |
| Rnd_ltr | TEXT |
| Split_Time | FLOAT |
| Split_no | INT |
| Team_ltr | TEXT |
| Team_no | LONG |

### Table: `StdLanes`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| order_01 | INT |
| order_02 | INT |
| order_03 | INT |
| order_04 | INT |
| order_05 | INT |
| order_06 | INT |
| order_07 | INT |
| order_08 | INT |
| order_09 | INT |
| order_10 | INT |
| order_11 | INT |
| order_12 | INT |
| tot_lanes | INT |

### Table: `TagNames`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| for_entryqual | BOOLEAN |
| for_scoring | BOOLEAN |
| for_timestd | BOOLEAN |
| tag_desc | TEXT |
| tag_name | TEXT |
| tag_ptr | LONG |

### Table: `Team`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| InvitedEntry_status | TEXT |
| InvitedFile_TMuploaddatetime | TEXT |
| InvitedFile_importdatetime | TEXT |
| InvitedFile_source | TEXT |
| InvitedFile_status | TEXT |
| InvitedHas_notes | BOOLEAN |
| InvitedLeague_name | TEXT |
| InvitedPayment_status | TEXT |
| InvitedTeam_AgencyID | LONG |
| InvitedTeam_Email | TEXT |
| Invited_Athletecount | TEXT |
| Invited_GovBody | TEXT |
| Invited_InviteCode | TEXT |
| Invited_TeamEntryID | LONG |
| Invited_TeamID | LONG |
| Invited_notes | TEXT |
| NoAthlete_surcharge | BOOLEAN |
| NoFacility_surcharge | BOOLEAN |
| NoRelayOnly_surcharge | BOOLEAN |
| NoTeam_surcharge | BOOLEAN |
| Team_Code | TEXT |
| Team_Gender | TEXT |
| Team_NoPoints | BOOLEAN |
| Team_Selected | BOOLEAN |
| Team_abbr | TEXT |
| Team_addr1 | TEXT |
| Team_addr2 | TEXT |
| Team_altabbr | TEXT |
| Team_altname | TEXT |
| Team_asst | TEXT |
| Team_c10 | TEXT |
| Team_c3 | TEXT |
| Team_c4 | TEXT |
| Team_c5 | TEXT |
| Team_c6 | TEXT |
| Team_c7 | TEXT |
| Team_c8 | TEXT |
| Team_c9 | TEXT |
| Team_cell | TEXT |
| Team_city | TEXT |
| Team_cntry | TEXT |
| Team_daytele | TEXT |
| Team_div | INT |
| Team_email | TEXT |
| Team_evetele | TEXT |
| Team_faxtele | TEXT |
| Team_head | TEXT |
| Team_name | TEXT |
| Team_no | LONG |
| Team_prov | TEXT |
| Team_region | INT |
| Team_short | TEXT |
| Team_stat | TEXT |
| Team_statenew | TEXT |
| Team_zip | TEXT |
| team_lsc | TEXT |

### Table: `TeamCoaches`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Coach_Cell | TEXT |
| Coach_Cert1 | TEXT |
| Coach_Cert2 | TEXT |
| Coach_Cert3 | TEXT |
| Coach_Cert4 | TEXT |
| Coach_EMail | TEXT |
| Coach_ExpDate1 | SHORT_DATE_TIME |
| Coach_ExpDate2 | SHORT_DATE_TIME |
| Coach_ExpDate3 | SHORT_DATE_TIME |
| Coach_ExpDate4 | SHORT_DATE_TIME |
| Coach_FirstName | TEXT |
| Coach_LastName | TEXT |
| Coach_Phone | TEXT |
| Coach_Title | TEXT |
| Coach_no | LONG |
| FemaleCoach_Only | BOOLEAN |
| MaleCoach_Only | BOOLEAN |
| Primary_FemaleHeadCoach | BOOLEAN |
| Primary_MaleHeadCoach | BOOLEAN |
| Team_no | LONG |

### Table: `TimeStd`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| div_abbr | TEXT |
| high_Age | INT |
| low_age | INT |
| tag_course | TEXT |
| tag_dist | LONG |
| tag_gender | TEXT |
| tag_indrel | TEXT |
| tag_ptr | LONG |
| tag_stroke | TEXT |
| tag_time | FLOAT |

### Table: `WaveOffset`
Found in 13 files.
Columns:
| Column | Type |
|---|---|
| Event_ptr | LONG |
| Heat_no | INT |
| Rnd_ltr | TEXT |
| Wave_offset | FLOAT |
