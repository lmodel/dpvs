---
search:
  boost: 10.0
---

# Class: LegalObligationImpaired 


_Justification that the process could not be fulfilled as it would impair_

_or conflict with a legal obligation_



<div data-search-exclude markdown="1">



URI: [justifications:LegalObligationImpaired](https://w3id.org/lmodel/dpv/justifications/LegalObligationImpaired)





```mermaid
 classDiagram
    class LegalObligationImpaired
    click LegalObligationImpaired href "../LegalObligationImpaired/"
      LegalProcessImpaired <|-- LegalObligationImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **LegalObligationImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegalObligationImpaired](https://w3id.org/lmodel/dpv/justifications/LegalObligationImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Required for Legal Obligation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegalObligationImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegalObligationImpaired |
| native | justifications:LegalObligationImpaired |
| exact | dpv_justifications:LegalObligationImpaired, dpv_justifications_owl:LegalObligationImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalObligationImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalObligationImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled as it would impair

  or conflict with a legal obligation'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Required for Legal Obligation
exact_mappings:
- dpv_justifications:LegalObligationImpaired
- dpv_justifications_owl:LegalObligationImpaired
is_a: LegalProcessImpaired
class_uri: justifications:LegalObligationImpaired

```
</details>

### Induced

<details>
```yaml
name: LegalObligationImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalObligationImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled as it would impair

  or conflict with a legal obligation'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Required for Legal Obligation
exact_mappings:
- dpv_justifications:LegalObligationImpaired
- dpv_justifications_owl:LegalObligationImpaired
is_a: LegalProcessImpaired
class_uri: justifications:LegalObligationImpaired

```
</details></div>