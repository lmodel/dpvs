---
search:
  boost: 10.0
---

# Class: LegallyExempted 


_Justification that the process could not be fulfilled or was not_

_successful because it falls under legal exemption i.e. a law allows the_

_non-fulfilment_



<div data-search-exclude markdown="1">



URI: [justifications:LegallyExempted](https://w3id.org/lmodel/dpv/justifications/LegallyExempted)





```mermaid
 classDiagram
    class LegallyExempted
    click LegallyExempted href "../LegallyExempted/"
      LegalProcessImpaired <|-- LegallyExempted
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **LegallyExempted**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegallyExempted](https://w3id.org/lmodel/dpv/justifications/LegallyExempted) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Legally Exempted




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegallyExempted |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegallyExempted |
| native | justifications:LegallyExempted |
| exact | dpv_justifications:LegallyExempted, dpv_justifications_owl:LegallyExempted |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegallyExempted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegallyExempted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it falls under legal exemption i.e. a law allows the

  non-fulfilment'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legally Exempted
exact_mappings:
- dpv_justifications:LegallyExempted
- dpv_justifications_owl:LegallyExempted
is_a: LegalProcessImpaired
class_uri: justifications:LegallyExempted

```
</details>

### Induced

<details>
```yaml
name: LegallyExempted
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegallyExempted
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it falls under legal exemption i.e. a law allows the

  non-fulfilment'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legally Exempted
exact_mappings:
- dpv_justifications:LegallyExempted
- dpv_justifications_owl:LegallyExempted
is_a: LegalProcessImpaired
class_uri: justifications:LegallyExempted

```
</details></div>