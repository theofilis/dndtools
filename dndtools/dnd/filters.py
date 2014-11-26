# -*- coding: utf-8 -*-

import django_filters2
from dnd.models import (
    Spell, DndEdition, SpellSchool, SpellSubSchool, SpellDescriptor, FeatCategory,
    CharacterClass, Rulebook, Domain, Feat, Skill, Item, Language, RaceType, ItemSlot,
    ItemProperty, Deity, Rule)
from dnd.filters_fields import FeatMultiPrerequisiteFieldFilter


def rulebook_choices(unknown_entry=True):
    rulebook_choices = [
        (edition.name,
         [(rulebook.slug, rulebook.name)
          for rulebook in edition.rulebook_set.all()])
        for edition in DndEdition.objects.all()]
    if unknown_entry:
        rulebook_choices.insert(0, ('', 'Unknown'))

    return rulebook_choices


def edition_choices(unknown_entry=True):
    edition_choices = [(edition.slug, edition.name) for edition in
                       DndEdition.objects.all()]
    if unknown_entry:
        edition_choices.insert(0, ('', 'Unknown'))

    return edition_choices


def spell_level_choices():
    spell_level_choices = [(i, i) for i in range(0, 10)]

    return spell_level_choices


def character_class_choices():
    character_class_choices = [
        (clazz.slug, clazz.name) for clazz in CharacterClass.objects.all()
    ]
    character_class_choices.insert(0, ('', 'Unknown'))

    return character_class_choices


def character_class_casting_choices():
    character_class_choices = [
        (clazz.slug, clazz.name) for clazz in
        CharacterClass.objects.filter(spellclasslevel__id__isnull=False).distinct()
    ]
    character_class_choices.insert(0, ('', 'Unknown'))

    return character_class_choices


def domain_choices():
    domain_choices = [
        (domain.slug, domain.name) for domain in Domain.objects.all()
    ]
    domain_choices.insert(0, ('', 'Unknown'))

    return domain_choices


class SpellFilter(django_filters2.FilterSet):
    school_choices = [(school.slug, school.name)
                      for school in SpellSchool.objects.all()]
    school_choices.insert(0, ('', 'Unknown'))

    sub_school_choices = [(sub_school.slug, sub_school.name)
                          for sub_school in SpellSubSchool.objects.all()]
    sub_school_choices.insert(0, ('', 'Unknown'))

    descriptor_choices = [(descriptor.slug, descriptor.name)
                          for descriptor in SpellDescriptor.objects.all()]
    descriptor_choices.insert(0, ('', 'Unknown'))

    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Spell name'
    )
    # noinspection PyShadowingBuiltins
    range = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    casting_time = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    spell_resistance = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    area = django_filters2.CharFilter(
        lookup_type='icontains'
    )
    duration = django_filters2.CharFilter(
        lookup_type='icontains'
    )
    saving_throw = django_filters2.CharFilter(
        lookup_type='icontains'
    )

    school__slug = django_filters2.ChoiceFilter(
        choices=school_choices, label='School'
    )
    sub_school__slug = django_filters2.ChoiceFilter(
        choices=sub_school_choices, label='Sub-school'
    )
    descriptors__slug = django_filters2.ChoiceFilter(
        choices=descriptor_choices, label='Descriptor'
    )
    verbal_component = django_filters2.BooleanFilter()
    somatic_component = django_filters2.BooleanFilter()
    material_component = django_filters2.BooleanFilter()
    arcane_focus_component = django_filters2.BooleanFilter()
    divine_focus_component = django_filters2.BooleanFilter()
    xp_component = django_filters2.BooleanFilter()

    rulebook__dnd_edition__slug = django_filters2.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    rulebook__slug = django_filters2.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    description = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    class_levels__slug = django_filters2.ChoiceFilter(
        choices=character_class_casting_choices(),
        help_text='Shows only classes with own spell lists',
        label='Class',
        grouped=True,
    )
    spellclasslevel__level = django_filters2.MultipleChoiceFilter(
        choices=spell_level_choices(),
        label='Level for class',
        help_text='Use ctrl to select more levels!',
        grouped=True,
    )
    domain_levels__slug = django_filters2.ChoiceFilter(
        choices=domain_choices(),
        label='Domain',
        grouped=True,
    )
    spelldomainlevel__level = django_filters2.MultipleChoiceFilter(
        choices=spell_level_choices(),
        label='Level for domain',
        help_text='Use ctrl to select more levels!',
        grouped=True,
    )

    class Meta:
        model = Spell
        fields = [
            'name', 'range', 'spell_resistance', 'area', 'duration', 'saving_throw', 'casting_time',
            'school__slug', 'sub_school__slug', 'descriptors__slug',
            'verbal_component', 'somatic_component', 'material_component',
            'arcane_focus_component', 'divine_focus_component',
            'xp_component', 'rulebook__slug', 'rulebook__dnd_edition__slug', 'description',
            'class_levels__slug', 'spellclasslevel__level',
            'domain_levels__slug', 'spelldomainlevel__level', ]


class SpellFilterAdmin(SpellFilter):
    verified = django_filters2.BooleanFilter(
    )

    class Meta:
        model = SpellFilter.Meta.model
        fields = ['verified', ] + SpellFilter.Meta.fields


class ItemFilter(django_filters2.FilterSet):
    type_choices = [itemType for itemType in Item.ITEM_TYPE]
    type_choices.insert(0, ('', 'Unknown'))

    item_slot_choices = [
        (itemSlot.slug, itemSlot.name) for itemSlot in
        ItemSlot.objects.all()
    ]
    item_slot_choices.insert(0, ('', 'Unknown'))

    property_choices = [
        (property.slug, property.name) for property in ItemProperty.objects.all()
    ]

    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Item name'
    )
    rulebook__dnd_edition__slug = django_filters2.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    rulebook__slug = django_filters2.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    type = django_filters2.ChoiceFilter(
        label='Item Type', choices=type_choices
    )
    body_slot__slug = django_filters2.ChoiceFilter(
        label='Body Slot', choices=item_slot_choices
    )
    price_bonus = django_filters2.NumberFilter(
        label='Price bonus'
    )
    price_gp = django_filters2.RangeFilter(
        label='Price in GP (range)',
    )
    property__slug = django_filters2.MultipleChoiceFilter(
        label='Property', choices=property_choices
    )

    class Meta:
        model = Item
        fields = ['name', 'rulebook__dnd_edition__slug', 'rulebook__slug',

                  'price_bonus', 'price_gp',
                  'type', 'body_slot__slug', 'property__slug']


class LanguageFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Language name'
    )

    class Meta:
        model = Language
        fields = ['name', ]


class CharacterClassFilter(django_filters2.FilterSet):
    character_class__name = django_filters2.CharFilter(
        lookup_type='icontains', label='Class name'
    )
    character_class__prestige = django_filters2.BooleanFilter()
    rulebook__slug = django_filters2.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    rulebook__dnd_edition__slug = django_filters2.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    required_bab = django_filters2.RangeFilter(
        label='Required Base Attack (range)',
    )
    skill_points = django_filters2.RangeFilter(
        label='Skill points/level (range)',
    )
    class_features = django_filters2.CharFilter(
        label='Class feature',
        lookup_type='icontains',
    )
    hit_die = django_filters2.RangeFilter(
        label='Hit die (range)',
    )

    class Meta:
        model = CharacterClass
        fields = ['character_class__name', 'rulebook__slug', 'rulebook__dnd_edition__slug',
                  'character_class__prestige',
                  'required_bab', 'skill_points',
                  'class_features', 'hit_die', ]


class RulebookFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains'
    )
    dnd_edition__slug = django_filters2.ChoiceFilter(
        label='Edition', choices=edition_choices()
    )

    class Meta:
        model = Rulebook
        fields = ['name', 'dnd_edition__slug', ]


class FeatFilter(django_filters2.FilterSet):
    feat_category_choices = [(feat_category.slug, feat_category.name)
                             for feat_category in FeatCategory.objects.all()]

    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Feat name'
    )
    feat_categories__slug = django_filters2.MultipleChoiceFilter(
        choices=feat_category_choices,
        label='Feat category'
    )
    rulebook__slug = django_filters2.MultipleChoiceFilter(
        choices=rulebook_choices(unknown_entry=False),
        label='Rulebook',
    )
    rulebook__dnd_edition__slug = django_filters2.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )
    description = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    benefit = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    special = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    normal = django_filters2.CharFilter(
        lookup_type='icontains',
    )
    prerequisite = FeatMultiPrerequisiteFieldFilter(
        label='Prerequisites',
    )

    class Meta:
        model = Feat
        fields = ['name', 'feat_categories__slug', 'rulebook__slug', 'rulebook__dnd_edition__slug', 'description',
                  'benefit', 'special',
                  'normal', ]


class SpellDomainFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Domain name'
    )

    class Meta:
        model = Domain
        fields = ['name', ]


class SpellDescriptorFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Descriptor name'
    )

    class Meta:
        model = SpellDescriptor
        fields = ['name', ]


class SkillFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains'
    )
    trained_only = django_filters2.BooleanFilter()
    armor_check_penalty = django_filters2.BooleanFilter()
    base_skill = django_filters2.ChoiceFilter(
        choices=(
            ('', 'Unknown'),
            ('STR', 'STR'),
            ('CON', 'CON'),
            ('DEX', 'DEX'),
            ('INT', 'INT'),
            ('WIS', 'WIS'),
            ('CHA', 'CHA'),
            ('None', 'None'),
        )
    )

    class Meta:
        model = Skill
        fields = ['name', 'trained_only', 'armor_check_penalty', 'base_skill']


class RuleFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains'
    )

    class Meta:
        model = Rule
        fields = ['name', ]


class DeityFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains'
    )

    class Meta:
        model = Deity
        fields = ['name']


class MonsterFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Monster name'
    )
    rulebook__slug = django_filters2.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    rulebook__dnd_edition__slug = django_filters2.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )

    class Meta:
        model = Spell
        fields = [
            'name', 'rulebook__slug', 'rulebook__dnd_edition__slug', ]


class RaceFilter(django_filters2.FilterSet):
    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Race name'
    )
    rulebook__slug = django_filters2.ChoiceFilter(
        label='Rulebook', choices=rulebook_choices()
    )
    rulebook__dnd_edition__slug = django_filters2.MultipleChoiceFilter(
        choices=edition_choices(unknown_entry=False),
        label='Edition',
    )

    class Meta:
        model = Spell
        fields = [
            'name', 'rulebook__slug', 'rulebook__dnd_edition__slug', ]


class RaceTypeFilter(django_filters2.FilterSet):
    save_type_choices = [raceTypePair for raceTypePair in RaceType.BASE_SAVE_TYPE_CHOICES]
    save_type_choices.insert(0, ('', 'Unknown'))

    base_attack_type_choices = [raceTypePair for raceTypePair in RaceType.BASE_ATTACK_TYPE_CHOICES]
    base_attack_type_choices.insert(0, ('', 'Unknown'))

    name = django_filters2.CharFilter(
        lookup_type='icontains', label='Race type name'
    )
    hit_die_size = django_filters2.RangeFilter(
        label='Hit Die Size',
        help_text='(range from-to)',
    )
    base_attack_type = django_filters2.ChoiceFilter(
        label='Base Attack Type', choices=base_attack_type_choices
    )
    base_fort_save_type = django_filters2.ChoiceFilter(
        label='Fort Save Type', choices=save_type_choices
    )
    base_reflex_save_type = django_filters2.ChoiceFilter(
        label='Reflex Save Type', choices=save_type_choices
    )
    base_will_save_type = django_filters2.ChoiceFilter(
        label='Will Save Type', choices=save_type_choices
    )

    class Meta:
        model = RaceType
        fields = ['name', 'hit_die_size', 'base_fort_save_type', 'base_reflex_save_type', 'base_will_save_type']