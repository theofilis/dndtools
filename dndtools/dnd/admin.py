# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from dnd.models import (FeatCategory, Skill, SpecialFeatPrerequisite, TextFeatPrerequisite,
                        FeatSpecialFeatPrerequisite, FeatRequiresFeat, Feat, FeatRequiresSkill,
                        CharacterClassVariant, RaceFavoredCharacterClass, Race, RaceSize, RaceSpeed,
                        RaceSpeedType, SkillVariant, NewsEntry, StaticPage, CharacterClassVariantRequiresFeat,
                        CharacterClassVariantRequiresRace, CharacterClassVariantRequiresSkill, MonsterHasFeat,
                        MonsterHasSkill, MonsterSpeed, Monster, MonsterSubtype, MonsterType, Rule, Item,
                        ItemSlot, ItemAuraType, ItemActivationType, ItemProperty, Language, RaceType, Deity,
                        DndEdition, Rulebook, CharacterClass, SpellDescriptor,
                        SpellSchool, SpellSubSchool, Spell, SpellClassLevel,
                        Domain, SpellDomainLevel, DomainVariant)


class ModifiedUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'last_login')


class DndEditionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'system', )
    list_display_links = ('name', )
    list_filter = ('system', )
    search_fields = ('name', )


class RulebookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'dnd_edition', )
    list_display_links = ('name', )
    list_filter = ('dnd_edition', )
    search_fields = ('name', )


class CharacterClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'prestige')
    list_display_links = ('name', )
    list_filter = ('prestige', )
    search_fields = ('name', )


class CharacterClassVariantRequiresRaceInline(admin.TabularInline):
    model = CharacterClassVariantRequiresRace
    extra = 3


class CharacterClassVariantRequiresFeatInline(admin.TabularInline):
    model = CharacterClassVariantRequiresFeat
    extra = 3


class CharacterClassVariantRequiresSkillInline(admin.TabularInline):
    model = CharacterClassVariantRequiresSkill
    extra = 3


class CharacterClassVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'character_class', 'rulebook', )
    list_filter = ('character_class', 'rulebook', )
    search_fields = ('character_class__name', )
    filter_horizontal = ('class_skills', )
    inlines = (
        CharacterClassVariantRequiresRaceInline, CharacterClassVariantRequiresFeatInline,
        CharacterClassVariantRequiresSkillInline,
    )


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'price_gp', 'price_bonus')
    list_display_links = ('name', )
    search_fields = ('name', )
    filter_horizontal = ('required_spells', 'aura_schools', 'required_feats', )


class ItemSlotAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


class ItemAuraTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


class ItemPropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


class ItemActivationTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


class DomainAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name',)
    list_display_links = ('name', )
    search_fields = ('name', )


class DomainVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'rulebook', )
    list_display_links = ('domain', )
    list_filter = ('domain', 'rulebook', )
    search_fields = ('domain__name', )
    filter_horizontal = ('deities', 'other_deities', )


class SpellDescriptorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class SpellSchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class SpellSubSchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class SpellClassLevelInline(admin.TabularInline):
    model = SpellClassLevel
    extra = 3


class SpellDomainLevelInline(admin.TabularInline):
    model = SpellDomainLevel
    extra = 3


class SpellAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'id', 'name', 'verified', 'verified_author', 'verified_time',
        'rulebook', 'page', 'school', 'sub_school',
    )
    list_display_links = ('name', )
    list_filter = ('verified', 'verified_author', 'rulebook',)
    date_hierarchy = 'verified_time'
    readonly_fields = ('verified', 'verified_author', 'verified_time', )
    search_fields = ('name', )
    inlines = (SpellClassLevelInline, SpellDomainLevelInline, )
    filter_horizontal = ('descriptors', )


class FeatCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class SkillAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'id', 'name', 'base_skill', 'trained_only', 'armor_check_penalty',
    )
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('base_skill', 'trained_only', 'armor_check_penalty',)


class SkillVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill', 'rulebook', )
    list_filter = ('skill', 'rulebook', )


class SpecialFeatPrerequisiteAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'print_format',
    )
    list_display_links = ('name', )
    search_fields = ('name', )


class TextFeatPrerequisiteInline(admin.TabularInline):
    model = TextFeatPrerequisite
    extra = 3


class FeatSpecialFeatPrerequisiteInline(admin.TabularInline):
    model = FeatSpecialFeatPrerequisite
    extra = 3


class FeatRequiresFeatInline(admin.TabularInline):
    model = FeatRequiresFeat
    extra = 3
    fk_name = 'source_feat'


class FeatRequiresSkillInline(admin.TabularInline):
    model = FeatRequiresSkill
    extra = 3


class FeatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'id', 'name', 'rulebook',
    )
    list_display_links = ('name', )
    list_filter = (
        'rulebook',
    )
    search_fields = ('name', )
    inlines = (
        TextFeatPrerequisiteInline, FeatSpecialFeatPrerequisiteInline,
        FeatRequiresSkillInline,
        FeatRequiresFeatInline,
    )


class MonsterTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class MonsterSubtypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class MonsterSpeedInline(admin.TabularInline):
    model = MonsterSpeed
    extra = 1


class MonsterHasFeatInline(admin.TabularInline):
    model = MonsterHasFeat
    extra = 3


class MonsterHasSkillInline(admin.TabularInline):
    model = MonsterHasSkill
    extra = 3


class MonsterSubtypeInline(admin.TabularInline):
    model = MonsterHasSkill
    extra = 3


class MonsterForm(forms.ModelForm):
    special_qualities = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Monster
        fields = ()


class MonsterAdmin(admin.ModelAdmin):
    form = MonsterForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'rulebook', )
    list_display_links = ('name', )
    list_filter = ('rulebook', )
    search_fields = ('name', )
    inlines = (
        MonsterSpeedInline, MonsterHasSkillInline, MonsterHasFeatInline,
    )


class RaceFavoredCharacterClassInline(admin.TabularInline):
    model = RaceFavoredCharacterClass
    extra = 1


class RaceSpeedInline(admin.TabularInline):
    model = RaceSpeed
    extra = 1


class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'id', 'name', 'rulebook', 'str', 'dex', 'con', 'int', 'wis', 'cha', 'level_adjustment',
    )
    list_display_links = ('name', )
    list_filter = (
        'rulebook',
    )
    search_fields = ('name', )
    inlines = (
        RaceFavoredCharacterClassInline, RaceSpeedInline
    )
    filter_horizontal = ('automatic_languages', 'bonus_languages', )


class RaceSizeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_display_links = ('name', )


class RaceSpeedTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'extra'
    )
    list_display_links = ('name', )


class NewsEntryAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'published', 'enabled',
    )
    date_hierarchy = 'published'


class StaticPageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class RuleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', )
    list_display = (
        'name',
    )


class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'name',
    )
    list_display_links = ('name', )
    search_fields = ('name', )


class RaceTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'name',
    )
    list_display_links = ('name', )
    search_fields = ('name', )


class DeityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'name',
    )
    list_display_links = ('name', )
    search_fields = ('name', )


admin.site.register(DndEdition, DndEditionAdmin)
admin.site.register(Rulebook, RulebookAdmin)
admin.site.register(CharacterClass, CharacterClassAdmin)
admin.site.register(CharacterClassVariant, CharacterClassVariantAdmin)
admin.site.register(SpellDescriptor, SpellDescriptorAdmin)
admin.site.register(SpellSchool, SpellSchoolAdmin)
admin.site.register(SpellSubSchool, SpellSubSchoolAdmin)
admin.site.register(Spell, SpellAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(FeatCategory, FeatCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillVariant, SkillVariantAdmin)
admin.site.register(SpecialFeatPrerequisite, SpecialFeatPrerequisiteAdmin)
admin.site.register(Feat, FeatAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(MonsterType, MonsterTypeAdmin)
admin.site.register(MonsterSubtype, MonsterSubtypeAdmin)
admin.site.register(Monster, MonsterAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(RaceSize, RaceSizeAdmin)
admin.site.register(RaceSpeedType, RaceSpeedTypeAdmin)
admin.site.register(RaceType, RaceTypeAdmin)
admin.site.register(NewsEntry, NewsEntryAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemSlot, ItemSlotAdmin)
admin.site.register(ItemProperty, ItemPropertyAdmin)
admin.site.register(ItemAuraType, ItemAuraTypeAdmin)
admin.site.register(ItemActivationType, ItemActivationTypeAdmin)
admin.site.register(Deity, DeityAdmin)
admin.site.register(DomainVariant, DomainVariantAdmin)
admin.site.unregister(User)
admin.site.register(User, ModifiedUserAdmin)
