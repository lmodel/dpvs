---
search:
  boost: 10.0
---

# Class: EmailAddressWork 


_Information about email address used for work or in professional_

_capacity_



<div data-search-exclude markdown="1">



URI: [pd:EmailAddressWork](https://w3id.org/lmodel/dpv/pd/EmailAddressWork)





```mermaid
 classDiagram
    class EmailAddressWork
    click EmailAddressWork href "../EmailAddressWork/"
      EmailAddress <|-- EmailAddressWork
        click EmailAddress href "../EmailAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [EmailAddress](EmailAddress.md)
            * **EmailAddressWork**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EmailAddressWork](https://w3id.org/lmodel/dpv/pd/EmailAddressWork) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Email Address Work




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EmailAddressWork |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EmailAddressWork |
| native | pd:EmailAddressWork |
| exact | dpv_pd:EmailAddressWork, dpv_pd_owl:EmailAddressWork |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EmailAddressWork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailAddressWork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about email address used for work or in professional

  capacity'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Address Work
exact_mappings:
- dpv_pd:EmailAddressWork
- dpv_pd_owl:EmailAddressWork
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: EmailAddress
class_uri: pd:EmailAddressWork

```
</details>

### Induced

<details>
```yaml
name: EmailAddressWork
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmailAddressWork
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about email address used for work or in professional

  capacity'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Email Address Work
exact_mappings:
- dpv_pd:EmailAddressWork
- dpv_pd_owl:EmailAddressWork
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: EmailAddress
class_uri: pd:EmailAddressWork

```
</details></div>