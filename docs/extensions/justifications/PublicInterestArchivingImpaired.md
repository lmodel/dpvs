---
search:
  boost: 10.0
---

# Class: PublicInterestArchivingImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it impairs archiving for public interest_



<div data-search-exclude markdown="1">



URI: [justifications:PublicInterestArchivingImpaired](https://w3id.org/lmodel/dpv/justifications/PublicInterestArchivingImpaired)





```mermaid
 classDiagram
    class PublicInterestArchivingImpaired
    click PublicInterestArchivingImpaired href "../PublicInterestArchivingImpaired/"
      LegalProcessImpaired <|-- PublicInterestArchivingImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **PublicInterestArchivingImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:PublicInterestArchivingImpaired](https://w3id.org/lmodel/dpv/justifications/PublicInterestArchivingImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Public Interest Archiving Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#PublicInterestArchivingImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:PublicInterestArchivingImpaired |
| native | justifications:PublicInterestArchivingImpaired |
| exact | dpv_justifications:PublicInterestArchivingImpaired, dpv_justifications_owl:PublicInterestArchivingImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicInterestArchivingImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicInterestArchivingImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it impairs archiving for public interest'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Interest Archiving Impaired
exact_mappings:
- dpv_justifications:PublicInterestArchivingImpaired
- dpv_justifications_owl:PublicInterestArchivingImpaired
is_a: LegalProcessImpaired
class_uri: justifications:PublicInterestArchivingImpaired

```
</details>

### Induced

<details>
```yaml
name: PublicInterestArchivingImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicInterestArchivingImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it impairs archiving for public interest'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Interest Archiving Impaired
exact_mappings:
- dpv_justifications:PublicInterestArchivingImpaired
- dpv_justifications_owl:PublicInterestArchivingImpaired
is_a: LegalProcessImpaired
class_uri: justifications:PublicInterestArchivingImpaired

```
</details></div>