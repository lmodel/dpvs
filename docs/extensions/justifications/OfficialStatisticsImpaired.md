---
search:
  boost: 10.0
---

# Class: OfficialStatisticsImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with official statistics_



<div data-search-exclude markdown="1">



URI: [justifications:OfficialStatisticsImpaired](https://w3id.org/lmodel/dpv/justifications/OfficialStatisticsImpaired)





```mermaid
 classDiagram
    class OfficialStatisticsImpaired
    click OfficialStatisticsImpaired href "../OfficialStatisticsImpaired/"
      LegalProcessImpaired <|-- OfficialStatisticsImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **OfficialStatisticsImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:OfficialStatisticsImpaired](https://w3id.org/lmodel/dpv/justifications/OfficialStatisticsImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Official Statistics Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#OfficialStatisticsImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:OfficialStatisticsImpaired |
| native | justifications:OfficialStatisticsImpaired |
| exact | dpv_justifications:OfficialStatisticsImpaired, dpv_justifications_owl:OfficialStatisticsImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OfficialStatisticsImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#OfficialStatisticsImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with official statistics'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Official Statistics Impaired
exact_mappings:
- dpv_justifications:OfficialStatisticsImpaired
- dpv_justifications_owl:OfficialStatisticsImpaired
is_a: LegalProcessImpaired
class_uri: justifications:OfficialStatisticsImpaired

```
</details>

### Induced

<details>
```yaml
name: OfficialStatisticsImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#OfficialStatisticsImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with official statistics'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Official Statistics Impaired
exact_mappings:
- dpv_justifications:OfficialStatisticsImpaired
- dpv_justifications_owl:OfficialStatisticsImpaired
is_a: LegalProcessImpaired
class_uri: justifications:OfficialStatisticsImpaired

```
</details></div>