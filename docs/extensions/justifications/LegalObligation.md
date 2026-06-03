---
search:
  boost: 10.0
---

# Class: LegalObligation 


_Justification that the process should be carried out due to it being a_

_legal obligation_



<div data-search-exclude markdown="1">



URI: [justifications:LegalObligation](https://w3id.org/lmodel/dpv/justifications/LegalObligation)





```mermaid
 classDiagram
    class LegalObligation
    click LegalObligation href "../LegalObligation/"
      ExerciseJustification <|-- LegalObligation
        click ExerciseJustification href "../ExerciseJustification/"
      
      
```





## Inheritance
* [ExerciseJustification](ExerciseJustification.md)
    * **LegalObligation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegalObligation](https://w3id.org/lmodel/dpv/justifications/LegalObligation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Legal Obligation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegalObligation |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegalObligation |
| native | justifications:LegalObligation |
| exact | dpv_justifications:LegalObligation, dpv_justifications_owl:LegalObligation |
| related | oscal:ResponsibilityStatement |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process should be carried out due to it being
  a

  legal obligation'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Obligation
exact_mappings:
- dpv_justifications:LegalObligation
- dpv_justifications_owl:LegalObligation
related_mappings:
- oscal:ResponsibilityStatement
is_a: ExerciseJustification
class_uri: justifications:LegalObligation

```
</details>

### Induced

<details>
```yaml
name: LegalObligation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalObligation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process should be carried out due to it being
  a

  legal obligation'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Obligation
exact_mappings:
- dpv_justifications:LegalObligation
- dpv_justifications_owl:LegalObligation
related_mappings:
- oscal:ResponsibilityStatement
is_a: ExerciseJustification
class_uri: justifications:LegalObligation

```
</details></div>