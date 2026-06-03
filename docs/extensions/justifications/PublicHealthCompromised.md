---
search:
  boost: 10.0
---

# Class: PublicHealthCompromised 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with necessary tasks carried out_

_for public health reasons_



<div data-search-exclude markdown="1">



URI: [justifications:PublicHealthCompromised](https://w3id.org/lmodel/dpv/justifications/PublicHealthCompromised)





```mermaid
 classDiagram
    class PublicHealthCompromised
    click PublicHealthCompromised href "../PublicHealthCompromised/"
      LegalProcessImpaired <|-- PublicHealthCompromised
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **PublicHealthCompromised**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:PublicHealthCompromised](https://w3id.org/lmodel/dpv/justifications/PublicHealthCompromised) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Public Health Compromised




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#PublicHealthCompromised |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:PublicHealthCompromised |
| native | justifications:PublicHealthCompromised |
| exact | dpv_justifications:PublicHealthCompromised, dpv_justifications_owl:PublicHealthCompromised |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicHealthCompromised
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicHealthCompromised
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks carried out

  for public health reasons'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Health Compromised
exact_mappings:
- dpv_justifications:PublicHealthCompromised
- dpv_justifications_owl:PublicHealthCompromised
is_a: LegalProcessImpaired
class_uri: justifications:PublicHealthCompromised

```
</details>

### Induced

<details>
```yaml
name: PublicHealthCompromised
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicHealthCompromised
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks carried out

  for public health reasons'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Health Compromised
exact_mappings:
- dpv_justifications:PublicHealthCompromised
- dpv_justifications_owl:PublicHealthCompromised
is_a: LegalProcessImpaired
class_uri: justifications:PublicHealthCompromised

```
</details></div>