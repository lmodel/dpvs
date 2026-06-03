---
search:
  boost: 10.0
---

# Class: ConsentProvided 


_Justification that the process could not be fulfilled or was not_

_successful because it is based on (a previously given) consent_



<div data-search-exclude markdown="1">



URI: [justifications:ConsentProvided](https://w3id.org/lmodel/dpv/justifications/ConsentProvided)





```mermaid
 classDiagram
    class ConsentProvided
    click ConsentProvided href "../ConsentProvided/"
      NonFulfilmentJustification <|-- ConsentProvided
        click NonFulfilmentJustification href "../NonFulfilmentJustification/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * **ConsentProvided**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ConsentProvided](https://w3id.org/lmodel/dpv/justifications/ConsentProvided) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Consent Provided




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ConsentProvided |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ConsentProvided |
| native | justifications:ConsentProvided |
| exact | dpv_justifications:ConsentProvided, dpv_justifications_owl:ConsentProvided |
| related | oscal:ResponsibilityStatement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConsentProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ConsentProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is based on (a previously given) consent'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Consent Provided
exact_mappings:
- dpv_justifications:ConsentProvided
- dpv_justifications_owl:ConsentProvided
related_mappings:
- oscal:ResponsibilityStatement
is_a: NonFulfilmentJustification
class_uri: justifications:ConsentProvided

```
</details>

### Induced

<details>
```yaml
name: ConsentProvided
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ConsentProvided
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is based on (a previously given) consent'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Consent Provided
exact_mappings:
- dpv_justifications:ConsentProvided
- dpv_justifications_owl:ConsentProvided
related_mappings:
- oscal:ResponsibilityStatement
is_a: NonFulfilmentJustification
class_uri: justifications:ConsentProvided

```
</details></div>