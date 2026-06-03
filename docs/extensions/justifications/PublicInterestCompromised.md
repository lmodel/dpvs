---
search:
  boost: 10.0
---

# Class: PublicInterestCompromised 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with necessary tasks carried out_

_for public interest_



<div data-search-exclude markdown="1">



URI: [justifications:PublicInterestCompromised](https://w3id.org/lmodel/dpv/justifications/PublicInterestCompromised)





```mermaid
 classDiagram
    class PublicInterestCompromised
    click PublicInterestCompromised href "../PublicInterestCompromised/"
      LegalProcessImpaired <|-- PublicInterestCompromised
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **PublicInterestCompromised**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:PublicInterestCompromised](https://w3id.org/lmodel/dpv/justifications/PublicInterestCompromised) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Public Interest Compromised




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#PublicInterestCompromised |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:PublicInterestCompromised |
| native | justifications:PublicInterestCompromised |
| exact | dpv_justifications:PublicInterestCompromised, dpv_justifications_owl:PublicInterestCompromised |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicInterestCompromised
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicInterestCompromised
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks carried out

  for public interest'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Interest Compromised
exact_mappings:
- dpv_justifications:PublicInterestCompromised
- dpv_justifications_owl:PublicInterestCompromised
is_a: LegalProcessImpaired
class_uri: justifications:PublicInterestCompromised

```
</details>

### Induced

<details>
```yaml
name: PublicInterestCompromised
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicInterestCompromised
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks carried out

  for public interest'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Interest Compromised
exact_mappings:
- dpv_justifications:PublicInterestCompromised
- dpv_justifications_owl:PublicInterestCompromised
is_a: LegalProcessImpaired
class_uri: justifications:PublicInterestCompromised

```
</details></div>