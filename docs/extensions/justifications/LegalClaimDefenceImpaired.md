---
search:
  boost: 10.0
---

# Class: LegalClaimDefenceImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the defence of legal claims_



<div data-search-exclude markdown="1">



URI: [justifications:LegalClaimDefenceImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimDefenceImpaired)





```mermaid
 classDiagram
    class LegalClaimDefenceImpaired
    click LegalClaimDefenceImpaired href "../LegalClaimDefenceImpaired/"
      LegalClaimImpaired <|-- LegalClaimDefenceImpaired
        click LegalClaimImpaired href "../LegalClaimImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * [LegalClaimImpaired](LegalClaimImpaired.md)
            * **LegalClaimDefenceImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegalClaimDefenceImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimDefenceImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Legal Claim Defence Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegalClaimDefenceImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegalClaimDefenceImpaired |
| native | justifications:LegalClaimDefenceImpaired |
| exact | dpv_justifications:LegalClaimDefenceImpaired, dpv_justifications_owl:LegalClaimDefenceImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalClaimDefenceImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimDefenceImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the defence of legal claims'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Defence Impaired
exact_mappings:
- dpv_justifications:LegalClaimDefenceImpaired
- dpv_justifications_owl:LegalClaimDefenceImpaired
is_a: LegalClaimImpaired
class_uri: justifications:LegalClaimDefenceImpaired

```
</details>

### Induced

<details>
```yaml
name: LegalClaimDefenceImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimDefenceImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the defence of legal claims'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Defence Impaired
exact_mappings:
- dpv_justifications:LegalClaimDefenceImpaired
- dpv_justifications_owl:LegalClaimDefenceImpaired
is_a: LegalClaimImpaired
class_uri: justifications:LegalClaimDefenceImpaired

```
</details></div>