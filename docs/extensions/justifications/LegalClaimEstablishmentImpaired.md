---
search:
  boost: 10.0
---

# Class: LegalClaimEstablishmentImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the establishment of legal_

_claims_



<div data-search-exclude markdown="1">



URI: [justifications:LegalClaimEstablishmentImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimEstablishmentImpaired)





```mermaid
 classDiagram
    class LegalClaimEstablishmentImpaired
    click LegalClaimEstablishmentImpaired href "../LegalClaimEstablishmentImpaired/"
      LegalClaimImpaired <|-- LegalClaimEstablishmentImpaired
        click LegalClaimImpaired href "../LegalClaimImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * [LegalClaimImpaired](LegalClaimImpaired.md)
            * **LegalClaimEstablishmentImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegalClaimEstablishmentImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimEstablishmentImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Legal Claim Establishment Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegalClaimEstablishmentImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegalClaimEstablishmentImpaired |
| native | justifications:LegalClaimEstablishmentImpaired |
| exact | dpv_justifications:LegalClaimEstablishmentImpaired, dpv_justifications_owl:LegalClaimEstablishmentImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalClaimEstablishmentImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimEstablishmentImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the establishment of legal

  claims'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Establishment Impaired
exact_mappings:
- dpv_justifications:LegalClaimEstablishmentImpaired
- dpv_justifications_owl:LegalClaimEstablishmentImpaired
is_a: LegalClaimImpaired
class_uri: justifications:LegalClaimEstablishmentImpaired

```
</details>

### Induced

<details>
```yaml
name: LegalClaimEstablishmentImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimEstablishmentImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the establishment of legal

  claims'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Establishment Impaired
exact_mappings:
- dpv_justifications:LegalClaimEstablishmentImpaired
- dpv_justifications_owl:LegalClaimEstablishmentImpaired
is_a: LegalClaimImpaired
class_uri: justifications:LegalClaimEstablishmentImpaired

```
</details></div>