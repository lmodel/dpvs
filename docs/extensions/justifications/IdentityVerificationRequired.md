---
search:
  boost: 10.0
---

# Class: IdentityVerificationRequired 


_Justification that the process could not be fulfilled or was not_

_successful because identity verification is required_



<div data-search-exclude markdown="1">



URI: [justifications:IdentityVerificationRequired](https://w3id.org/lmodel/dpv/justifications/IdentityVerificationRequired)





```mermaid
 classDiagram
    class IdentityVerificationRequired
    click IdentityVerificationRequired href "../IdentityVerificationRequired/"
      DelayJustification <|-- IdentityVerificationRequired
        click DelayJustification href "../DelayJustification/"
      
      
```





## Inheritance
* [DelayJustification](DelayJustification.md)
    * **IdentityVerificationRequired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:IdentityVerificationRequired](https://w3id.org/lmodel/dpv/justifications/IdentityVerificationRequired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Identity Verification Required




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#IdentityVerificationRequired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:IdentityVerificationRequired |
| native | justifications:IdentityVerificationRequired |
| exact | dpv_justifications:IdentityVerificationRequired, dpv_justifications_owl:IdentityVerificationRequired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IdentityVerificationRequired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#IdentityVerificationRequired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because identity verification is required'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Identity Verification Required
exact_mappings:
- dpv_justifications:IdentityVerificationRequired
- dpv_justifications_owl:IdentityVerificationRequired
is_a: DelayJustification
class_uri: justifications:IdentityVerificationRequired

```
</details>

### Induced

<details>
```yaml
name: IdentityVerificationRequired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#IdentityVerificationRequired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because identity verification is required'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Identity Verification Required
exact_mappings:
- dpv_justifications:IdentityVerificationRequired
- dpv_justifications_owl:IdentityVerificationRequired
is_a: DelayJustification
class_uri: justifications:IdentityVerificationRequired

```
</details></div>