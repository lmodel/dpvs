---
search:
  boost: 10.0
---

# Class: IdentityVerificationFailure 


_Justification that the process could not be fulfilled or was not_

_successful because identity verification failed_



<div data-search-exclude markdown="1">



URI: [justifications:IdentityVerificationFailure](https://w3id.org/lmodel/dpv/justifications/IdentityVerificationFailure)





```mermaid
 classDiagram
    class IdentityVerificationFailure
    click IdentityVerificationFailure href "../IdentityVerificationFailure/"
      SecurityImpaired <|-- IdentityVerificationFailure
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- IdentityVerificationFailure
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **IdentityVerificationFailure** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:IdentityVerificationFailure](https://w3id.org/lmodel/dpv/justifications/IdentityVerificationFailure) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Identity Verification Failure




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#IdentityVerificationFailure |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:IdentityVerificationFailure |
| native | justifications:IdentityVerificationFailure |
| exact | dpv_justifications:IdentityVerificationFailure, dpv_justifications_owl:IdentityVerificationFailure |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IdentityVerificationFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#IdentityVerificationFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because identity verification failed'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Identity Verification Failure
exact_mappings:
- dpv_justifications:IdentityVerificationFailure
- dpv_justifications_owl:IdentityVerificationFailure
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:IdentityVerificationFailure

```
</details>

### Induced

<details>
```yaml
name: IdentityVerificationFailure
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#IdentityVerificationFailure
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because identity verification failed'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Identity Verification Failure
exact_mappings:
- dpv_justifications:IdentityVerificationFailure
- dpv_justifications_owl:IdentityVerificationFailure
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:IdentityVerificationFailure

```
</details></div>