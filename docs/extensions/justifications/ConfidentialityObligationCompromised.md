---
search:
  boost: 10.0
---

# Class: ConfidentialityObligationCompromised 


_Justification that the process could not be fulfilled or was not_

_successful because it would compromise a confidentiality obligation_



<div data-search-exclude markdown="1">



URI: [justifications:ConfidentialityObligationCompromised](https://w3id.org/lmodel/dpv/justifications/ConfidentialityObligationCompromised)





```mermaid
 classDiagram
    class ConfidentialityObligationCompromised
    click ConfidentialityObligationCompromised href "../ConfidentialityObligationCompromised/"
      LegalProcessImpaired <|-- ConfidentialityObligationCompromised
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **ConfidentialityObligationCompromised**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ConfidentialityObligationCompromised](https://w3id.org/lmodel/dpv/justifications/ConfidentialityObligationCompromised) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Confidentiality Obligation Compromised




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ConfidentialityObligationCompromised |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ConfidentialityObligationCompromised |
| native | justifications:ConfidentialityObligationCompromised |
| exact | dpv_justifications:ConfidentialityObligationCompromised, dpv_justifications_owl:ConfidentialityObligationCompromised |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConfidentialityObligationCompromised
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ConfidentialityObligationCompromised
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would compromise a confidentiality obligation'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Confidentiality Obligation Compromised
exact_mappings:
- dpv_justifications:ConfidentialityObligationCompromised
- dpv_justifications_owl:ConfidentialityObligationCompromised
is_a: LegalProcessImpaired
class_uri: justifications:ConfidentialityObligationCompromised

```
</details>

### Induced

<details>
```yaml
name: ConfidentialityObligationCompromised
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ConfidentialityObligationCompromised
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would compromise a confidentiality obligation'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Confidentiality Obligation Compromised
exact_mappings:
- dpv_justifications:ConfidentialityObligationCompromised
- dpv_justifications_owl:ConfidentialityObligationCompromised
is_a: LegalProcessImpaired
class_uri: justifications:ConfidentialityObligationCompromised

```
</details></div>